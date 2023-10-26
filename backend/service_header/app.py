from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from openpyxl import load_workbook
from io import BytesIO
import mysql.connector
import json
import requests

import re
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

def extract_hospital(filename):
    # This regular expression matches anything up to the first underscore, then captures everything up to the second underscore
    match = re.search(r'^[^_]+_([^_]+)_', filename)

    # Check if we found a match
    if match:
        hospital = match.group(1)  # The first capture group is the hospital
        return hospital
    else:
        return None
    
def extract_operation(filename):
    # This regular expression has a single capture group that gets the string after the second underscore and before the next underscore or dot.
    match = re.search(r'([^_]+)_([^_]+)_([^.]+)', filename)

    # Check if we found a match
    if match:
        operation = match.group(3)  # The third capture group is the operation type
        return operation
    else:
        return None

def connect_to_database():
    db = mysql.connector.connect(
        host='host.docker.internal',
        port=3306,
        user='etienne',
        password='password',
        database='ter'
    )
    return db

@app.route('/mapping_header', methods=['POST'])
def mapping_header_():
    type_fichier = request.form.get('type_fichier')
    if type_fichier is None or type_fichier == "":
        return jsonify({"error" : "Missing type_fichier in request body"}), 400


    if 'file' not in request.files:
        return jsonify({"error" : "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error" : "No file part"}), 400
    
    if file and file.filename.endswith('.xlsx'):
        
        #Connection à la base pour tester si le type de fichier existe
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("SELECT TypeFichier FROM mandatoryfieldfiletype")
        existing_types = [row[0] for row in cursor.fetchall()]
        if type_fichier not in existing_types:
            return jsonify({'error': 'Type de fichier invalide', 'type_possible' : existing_types, "typefichier" : type_fichier}), 400

        
        #Si le fichier existe lecture du fichier est récupération des headers
        in_memory_file = BytesIO(file.read())
        workbook = load_workbook(in_memory_file, read_only=True, data_only=True)
        sheet = workbook.active  # Get the active sheet
        header_row = [cell.value for cell in sheet[1]]
        
        #Récupération du mapping 
        cursor.execute("SELECT FieldMapping.FileInputField, FieldMapping.FieldOutputField "
               "FROM FieldMapping "
               "JOIN FileTypeMapping ON FieldMapping.ID = FileTypeMapping.FieldMappingID "
               "WHERE FileTypeMapping.FileType = %s", (type_fichier,))
        results = cursor.fetchall()
        mapping_table = dict(results)

        #Test mapping 
        mapped_headers = {}
        unmapped_headers = []
        
        for header in header_row : 
            testing_header_exist_mapping = mapping_table.get(header)
            
            if testing_header_exist_mapping : 
                mapped_headers[header] = mapping_table.pop(header)
            else : 
                unmapped_headers.append(header)
        
        return jsonify({'mapped_headers' : mapped_headers, 'unmapped_headers':unmapped_headers, 'mapped_table_remaining_possibility' : list(mapping_table.values())})
    return jsonify({'error': 'Invalid file format'}), 400

@app.route('/check_header', methods=['POST'])
def check_header():
    type_fichier = request.form.get('type_fichier')
    if type_fichier is None or type_fichier == "":
        return jsonify({"error" : "Missing type_fichier in request body"}), 400
    mapping = request.form.get('mapping')
    if mapping is None or mapping == "": 
        return jsonify({"error" :  "Missing mapping in request body"}), 400
    
    #Connection à la base pour tester les mandatorys fields
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute("SELECT MandatoryField FROM mandatoryfieldfiletype WHERE TypeFichier=%s",(type_fichier,))
    results = cursor.fetchall()
    mandatory_fields = [item for tuple in results for set in tuple for item in set]
    
    if type_fichier == "Encounter" : 
        nom_fichier = request.form.get('nom_fichier')
        if extract_hospital(nom_fichier) is not None or "":
             mandatory_fields.remove("HOSPITAL")
    
    if len(mandatory_fields)  == 0 : 
        return jsonify({'error' : 'Le type de Fichier n"existe pas dans la base', 'typefichier' : type_fichier}), 400
    try:
        mapping_dict = json.loads(mapping)  # Parse the string into a dictionary
    except json.JSONDecodeError:
        return jsonify({"error" :  "Invalid mapping JSON format"}), 400
    
    missing_fields = [field for field in mandatory_fields if field not in mapping_dict.values()]
        
    if missing_fields:
        response = requests.post('http://rapport:5007/rapport_mandatory_fields', json={'mandatory_fields_missing': missing_fields, 'mandatory_fields': mandatory_fields, 'file_fields' : list(mapping_dict.values())}, timeout=10)
        if response.status_code == 200:
            buffer = BytesIO()
            buffer.write(response.content)
            buffer.seek(0)
            return send_file(buffer, download_name='rapport_mandatory_fields.xlsx', as_attachment=True, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        else:
            return jsonify({'error': 'Une erreur est survenue lors de la création du rapport.'}), 500

    return jsonify({'message': 'Tous les champs obligatoires sont présents.', 'value' : True})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5006)