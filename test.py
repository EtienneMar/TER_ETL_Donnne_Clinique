import requests
import os 

with open("../data/dataTer/_Fichier_Patient.xlsx", 'rb') as f:
    nifi_response = requests.post('http://localhost:5011/Patient', files={'file': f},timeout=120)