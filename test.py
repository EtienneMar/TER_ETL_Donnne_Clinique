from flask import Flask, jsonify, request
from flask_cors import CORS
from openpyxl import load_workbook
from io import BytesIO
import mysql.connector
import json
from werkzeug.utils import secure_filename
import re


def connect_to_database():
    db = mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='root',
        database='ter'
    )
    return db

def check_header(type_fichier ):
    #type_fichier = request.form.get('type_fichier')
    #if type_fichier is None or type_fichier == "":
    #    return jsonify({"error" : "Missing type_fichier in request body"}), 400
    #mapping = request.form.get('mapping')
    #if mapping is None or mapping == "": 
    #    return jsonify({"error" :  "Missing mapping in request body"}), 400
    
    #Connection à la base pour tester les mandatorys fields
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute("SELECT MandatoryField FROM mandatoryfieldfiletype WHERE TypeFichier=%s",(type_fichier,))
    results = cursor.fetchall()
    mandatory_fields = [item for tuple in results for set in tuple for item in set]
    print(mandatory_fields)
    print(type(mandatory_fields))
    if len(mandatory_fields)  == 0 : 
        return jsonify({'error' : 'Le type de Fichier n"existe pas dans la base', 'typefichier' : type_fichier}), 400
    #try:
    #    mapping_dict = json.loads(mapping)  # Parse the string into a dictionary
    #except json.JSONDecodeError:
    #    return jsonify({"error" :  "Invalid mapping JSON format"}), 400
    
    #missing_fields = [field for field in mandatory_fields if field not in mapping_dict.values()]

    #if missing_fields:
    #    return jsonify({'error': '1 ou plus des MandatoryFields sont manquants', 'mandatory_fields': missing_fields}), 400

check_header("Patient")
check_header("Transfer")