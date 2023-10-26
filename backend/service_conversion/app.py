import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from io import BytesIO
import numpy as np
import json
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


app = Flask(__name__)
CORS(app)    

#TODO Simplifier la conversion et le faire directement sur Nifi ? 
    # Pour cela il faudrait faire plusieurs webService dans Nifi en fonction du fichier ou changer le script de conversion. 

@app.route('/', methods=['GET'])
def home_test():
    return jsonify("conversion up")

@app.route('/excel-to-json', methods=['POST'])
def excel_to_json(): 
    if 'file' not in request.files:
        return jsonify({"error" : "No file part"}), 400
    file = request.files['file']
    if file.filename == '' : 
        return jsonify({"error" : "No file part"}), 400
    mapping = request.form.get('mapping')
    logger.debug(mapping)

    if file and file.filename.endswith('.xlsx'): 
        in_memory_file = BytesIO(file.read())
        # Read the Excel file into a DataFrame
        df = pd.read_excel(in_memory_file)
        # Replace Nan with None so the Json can read it 
        df = df.replace({np.nan: None})
        data = df.to_dict(orient="records")
        json_data = json.dumps(data, default=str, ensure_ascii=False)
        return jsonify(json_data)
    return jsonify({'error': 'Invalid file format'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)