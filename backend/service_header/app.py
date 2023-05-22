from flask import Flask, jsonify, request
from flask_cors import CORS
from openpyxl import load_workbook
from io import BytesIO
import mysql.connector
import json
from werkzeug.utils import secure_filename
import re

app = Flask(__name__)
CORS(app)

def extract_hospital(filename):
    # This regular expression has a single capture group that gets the words between the first and second underscore
    match = re.search(r'([^_]+)_([^_]+)', filename)

    # Check if we found a match
    if match:
        hospital = match.group(2)  # The second capture group is the hospital
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
        port=3307,
        user='root',
        password='root',
        database='ter'
    )
    return db

@app.route('/mapping_header', methods=['POST'])
def mapping_header_():
    print(request.form, request.files)
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
        cursor.execute("SELECT typeFichier FROM fichiertype")
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
        
        return jsonify({'mapped_headers' : mapped_headers, 'unmapped_headers':unmapped_headers, 'mapped_table_remaining_possibility' : mapping_table})
    return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5006)