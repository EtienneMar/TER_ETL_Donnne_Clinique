import os
import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def home_test():
    response = requests.get('http://conversion:5001/')
    if response.status_code == 200:
        json_data = response.json()

    return jsonify("stockage up"+json_data)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Call convert excel to json microservice
        with open(file_path, 'rb') as f:
            response = requests.post('http://conversion:5001/excel-to-json', files={'file': f})

        if response.status_code == 200:
            json_data = response.json()

            # Save each worksheet as a separate JSON file
            for sheet_name, sheet_data in json_data.items():
                json_file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{sheet_name}.json")
                with open(json_file_path, 'w') as json_file:
                    json.dump(sheet_data, json_file)
                    
             # Send JSON data to NiFi
            with open(json_file_path, 'rb') as f:
                nifi_response = requests.post('http://nifi:5003/requestListener', files={'file': f})
            if nifi_response.status_code == 200 : 
                rules_response = request.post('http://rules:5004/rules', json=nifi_response.json())
                
              # Check if NiFi request was successful
            if nifi_response.status_code != 200:
                return jsonify({"error": "Error sending JSON to NiFi"}), 500

            

            os.remove(file_path)

            return jsonify({"message": "Upload successful and JSON files created"}), 200
        else:
            os.remove(file_path)
            return jsonify({"error": "Error in converting Excel to JSON"}), 500

    else:
        return jsonify({"error": "File not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

