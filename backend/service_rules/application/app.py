import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import simplejson 
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rules import Rules


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home_test():
    return jsonify("service_rules up")

@app.route('/rules', methods=['POST'])
def rules_to_apply(): 
    if request.method == 'POST':
        # Récupère les données JSON envoyées dans la requête POST
        data = request.get_json()
        dfReject = pd.DataFrame()
        rules = Rules(pd.DataFrame(data),dfReject)
        rules.set_df(rules.get_df().drop_duplicates())
        
        columns_to_check = ["FathersName", "FathersPreName"]

        if all(column in rules.get_df().columns for column in columns_to_check):
            rules.v_lenght(100, ["FathersName", "FathersPreName"], ["PatientNumber"])
        # Renvoie une réponse indiquant que la requête a été traitée avec succès
        
        # Convertir les dataframes en dictionnaires
        df_dict = rules.get_df().to_dict(orient='records')
        df_reject_dict = rules.get_dfRejected().to_dict(orient='records')
        print(df_reject_dict)
        
        # Créer un dictionnaire plus grand pour contenir les deux
        response_dict = {'df': df_dict, 'df_rejected': df_reject_dict}
        
        # Renvoie une réponse indiquant que la requête a été traitée avec succès
        response = simplejson.dumps(response_dict, ignore_nan=True)
        return response, 200
    else:
        # Si la requête n'est pas une requête POST, renvoie une erreur 405 (Method Not Allowed)
        return 'Méthode non autorisée', 405

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)