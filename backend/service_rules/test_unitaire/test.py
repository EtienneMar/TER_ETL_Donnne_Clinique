import unittest
import pandas as pd
from flask import Flask, requests
import rules as Rules  # Remplacez 'your_module' par le nom du fichier contenant la classe Rules

SERVER_URL = 'http://localhost:5004'

class TestRulesWebService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_rules_endpoint_removes_duplicates(self):
        # Créer un DataFrame de test avec des duplicatas et le convertir en JSON
        test_data = {'A': [1, 2, 2, 3], 'B': [4, 5, 5, 6]}
        df = pd.DataFrame(test_data)
        df_json = df.to_json(orient='split')

        # Créer un DataFrame de référence sans duplicatas
        ref_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        ref_df = pd.DataFrame(ref_data)

        # Envoyer une requête POST au point de terminaison /rules
        response = requests.post(f'{SERVER_URL}/rules', json=df_json)

        # Vérifier si la réponse est un succès (code 200)
        self.assertEqual(response.status_code, 200)

        # Convertir la réponse JSON en DataFrame et vérifier si elle est égale au DataFrame de référence
        response_df = pd.read_json(response.json(), orient='split')
        pd.testing.assert_frame_equal(response_df, ref_df)

if __name__ == "__main__":
    unittest.main()