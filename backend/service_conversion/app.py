import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from io import BytesIO
import numpy as np
from convertdate import islamic
from dateutil.parser import parse, ParserError
from datetime import datetime


app = Flask(__name__)
CORS(app)


def convert_date(date_string):
    hijri_year = islamic.from_gregorian(datetime.now().year, datetime.now().month, datetime.now().day)[0]
    if len(date_string) >= 10:
        try:
            dt = parse(date_string)
            if dt.year <= hijri_year :
                date_convertie = islamic.to_gregorian(dt.year, dt.month, dt.day)
                date_convertie = dt.replace(year=date_convertie[0], month=date_convertie[1], day=date_convertie[2])
                return date_convertie.strftime("%Y-%m-%d %H:%M:%S")
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except ParserError:
            pass
    else : 
        return date_string

def convert_date_format(date_string):
    dt = pd.to_datetime(date_string, errors='coerce')
    if pd.isnull(dt):
        return None
    # Check if the original string contains all date parts
    elif any(part not in date_string for part in [str(dt.year), str(dt.month), str(dt.day), str(dt.hour), str(dt.minute), str(dt.second)]):
        return date_string
    else:
        return dt.strftime("%Y-%m-%d %H:%M:%S")

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
    if file and file.filename.endswith('.xlsx'): 
        in_memory_file = BytesIO(file.read())
        df = pd.read_excel(in_memory_file)
        colonne_date = df.select_dtypes(include=[np.datetime64]).columns.tolist()
        for col in colonne_date:
            df[col] = df[col].apply(convert_date)
        json_data = df.to_json() # na="null"
        return jsonify(json_data)
    return jsonify({'error': 'Invalid file format'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)