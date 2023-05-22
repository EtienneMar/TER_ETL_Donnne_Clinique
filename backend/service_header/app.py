from flask import Flask, jsonify, request
from flask_cors import CORS
from openpyxl import load_workbook
from io import BytesIO
import mysql.connector
import json

app = Flask(__name__)
CORS(app)



def connect_to_database():
    db = mysql.connector.connect(
        host='host.docker.internal',
        port=3307,
        user='root',
        password='root',
        database='ter'
    )
    return db

@app.route('/testing_header', methods=['POST'])
def testing_header_():
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
        in_memory_file = BytesIO(file.read())
        workbook = load_workbook(in_memory_file, read_only=True, data_only=True)
        sheet = workbook.active  # Get the active sheet
        header_row = [cell.value for cell in sheet[1]]
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("SELECT typeFichier FROM fichier_table")
        existing_types = [row[0] for row in cursor.fetchall()]
        if type_fichier not in existing_types:
            return jsonify({'error': 'Type de fichier invalide'}), 400
        cursor.execute("SELECT mandatoryField FROM fichier_table WHERE typeFichier = %s", (type_fichier,))
        mandatory_fields = cursor.fetchone()[0]
        mandatory_fields = json.loads(mandatory_fields)
        missing_fields = []
        for mandatory_field in mandatory_fields:
            if mandatory_field not in header_row:
                missing_fields.append(mandatory_field)
        if missing_fields:
            return jsonify({'error': 'Champs obligatoires manquants', 'missing_fields': missing_fields, 'header' : header_row}), 400
    
        return jsonify(header_row)
    return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5006)