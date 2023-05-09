import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import simplejson 


from backend.service_rules.rules import Rules

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
        rules = Rules(pd.read_json(data),dfReject)
        rules.set_df(rules.get_df().drop_duplicates())
        #rules.v_lenght(100, ["FathersName", "FathersPreName"], "PatientNumber")
        
        
        # Renvoie une réponse indiquant que la requête a été traitée avec succès
        response = simplejson.dumps(rules.get_df(), ignore_nan=True)
        return response, 200
    else:
        # Si la requête n'est pas une requête POST, renvoie une erreur 405 (Method Not Allowed)
        return 'Méthode non autorisée', 405

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)