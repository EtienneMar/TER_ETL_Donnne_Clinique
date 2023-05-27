import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from openpyxl import load_workbook
from io import BytesIO

app = Flask(__name__)
CORS(app)

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
        worbook = load_workbook(in_memory_file)
        json_data = {}
        for sheet in worbook.worksheets : 
            sheet_data = []
            for i in range(1, sheet.max_row):
                row = {}
                for j in range(1, sheet.max_column+1):
                    column_name = sheet.cell(row=1, column=j)
                    row_data = sheet.cell(row=i+1, column=j)
                    row.update({column_name.value: row_data.value})
                sheet_data.append(row)

            json_data[sheet.title] = sheet_data
        return jsonify(json_data)
    return jsonify({'error': 'Invalid file format'}), 400

@app.route('/convert_dates', methods=['POST'])
def convert_dates():
    data = request.get_json(force=True)
    for item in data:
        if item['BIRTHDATE']:
            item['BIRTHDATE'] = convert_date_format(item['BIRTHDATE'])
        if item['DATE_REGESITER']:
            item['DATE_REGESITER'] = convert_date_format(item['DATE_REGESITER'])
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)