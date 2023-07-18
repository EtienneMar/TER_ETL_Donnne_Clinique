import os
import requests
import json
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import urllib3
from http.cookies import SimpleCookie
from io import BytesIO
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
        return jsonify({"error": "No file part"}), 400 #Il n'y a pas de clé dans la requete 
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400 #Il n'y a pas de valeur dans l'ensemble clé valeur ou bien elle est nul
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
    mapping_str = request.form.get('mapping')
    if mapping_str is None or mapping_str == "": 
        return jsonify({"error" :  "Missing mapping in request body"}), 400
    mapping = json.loads(mapping_str)
    
    #APPEL DU JSON POUR MODIFIER LE MAPPING 
    # Disable the insecure request warning
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = 'https://172.19.0.8:8443/nifi-api/access/token'
    username = '6fce31dc-a3ef-4aba-94fc-535d43cca842'
    password = 'qDNgACY9tCsBUUVkQTGdRUKlSHQZfdcM'

    # Construct the request payload as form data
    data = {
        'username': username,
        'password': password
    }

    # Send the POST request with proper certificate verification and form data
    response_access_token = requests.post(url, data=data, verify=False, timeout=60)
    
    cookie = SimpleCookie()
    cookie.load(response_access_token.headers['Set-Cookie'])
    bearer_token = cookie['__Secure-Authorization-Bearer'].value



    url2 = 'https://172.19.0.8:8443/nifi-api/processors/364f1b18-31d9-1aee-2445-d72a6d0a4946'
    headers2 = {
        'Authorization': f'Bearer {bearer_token}'
    }

    #Calling Nifi API for get the process Version
    response_get_processor = requests.get(url2, headers=headers2, verify=False, timeout=60)
    json_data = json.loads(response_get_processor.content.decode('utf-8'))
    version_revision = json_data['revision']['version']
    
    #Handling the process Running to permit the overwrite
    if json_data['component']['state'] == "RUNNING" : 
        url = 'https://172.19.0.8:8443/nifi-api/processors/364f1b18-31d9-1aee-2445-d72a6d0a4946/run-status'  # Replace {id} with actual processor id

        data = {
            "revision": {
                "version": version_revision
            },
            "state": "STOPPED"  # Update this to the desired state
        }
        requests.put(url, headers=headers2, json=data, verify=False, timeout=60)
        #Changing the value of the version
        version_revision +=1
    
    #Getting the joltspec from the processor
    jolt_spec = json_data['component']['config']['properties']['jolt-spec']
    operations = json.loads(jolt_spec)

    #Changing the value of the mappingUser received in by the frontend and reverse the dictionnary 
    #Reversing is use to be more faster in searching the value in jolt
    for key, value in mapping.items():
        mapping[key] = f"FichierPatient[&1].{value.split('.')[-1]}"

    inverted_mapping = {v: k for k, v in mapping.items()}

    #Create the jolt specifiation for mapping
    for operation in operations:
        if operation['operation'] == 'shift':
            shift_spec = operation['spec']['*']
            for key, value in list(shift_spec.items()):
                if value in inverted_mapping and key != inverted_mapping[value]:
                    shift_spec[inverted_mapping[value]] = value
                    del shift_spec[key]
    #Sending the change for the processor
    spec = {
        "revision": {
                "version": version_revision
        },
        "component": {
            "id": json_data["component"]["id"],  # The processor ID
            "config" : {
                "properties": {
                    "jolt-spec" : f"{json.dumps(operations)}"
                }
            },
            "state": "RUNNING" 
        }    
    }

    response_modify_mapping = requests.put(url2, headers=headers2, verify=False, json=spec, timeout=60)

    if response_modify_mapping.status_code == 200 : 
        with open(file_path, 'rb') as f:
            response_conversion_excel_to_json = requests.post('http://conversion:5001/excel-to-json', files={'file': f}, timeout=120)
        if response_conversion_excel_to_json.status_code == 200:
            json_data = response_conversion_excel_to_json.json()
            # Save each worksheet as a separate JSON file
            for sheet_name, sheet_data in json_data.items():
                json_file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{sheet_name}.json")
                with open(json_file_path, 'w') as json_file:
                    json.dump(sheet_data, json_file)   
                    
                    
             # Send JSON data to NiFi ENVOIE DANS LE REQUEST LISTENER HANDLE HTTP 
            with open(json_file_path, 'rb') as f:
                nifi_response = requests.post('http://nifi:5011/requestListener', files={'file': f},timeout=120)
            if nifi_response.status_code == 200 : 
                fichier_traite = nifi_response.json()
                rapport_response = requests.post('http://rapport:5007/rapport', json=fichier_traite, timeout=120)
                if rapport_response.status_code == 200:
                    buffer = BytesIO()
                    buffer.write(rapport_response.content)
                    buffer.seek(0)
                    return send_file(buffer, download_name='rapport_mandatory_fields.xlsx', as_attachment=True, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
              # Check if NiFi request was successful
            else :
                return jsonify({"error": "Error sending JSON to NiFi", "nifi_response" : nifi_response.text }), nifi_response.status_code
        else : 
            os.remove(file_path)
            return jsonify({"error": "Error in converting Excel to JSON","Excel_response" : response_conversion_excel_to_json.text }), response_conversion_excel_to_json.status_code
    else : 
        return jsonify({"Erreur" : "impossible de réaliser le mappage Nifi", "response_nifi" : response_modify_mapping.text}), response_modify_mapping.status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

