import unittest
import pandas as pd
import json
import sys
import os
from flask import Flask

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from application.app import app  # Import correct

SERVER_URL = 'http://localhost:5004'

class TestRulesWebService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Utilisez le client de test correct
        self.app.testing = True
        
    def process_testing_only_df(self, test_data, ref_data):
        # Envoyer une requête POST au point de terminaison /rules
        response = self.app.post(f'{SERVER_URL}/rules', json=test_data)

        # Vérifier si la réponse est un succès (code 200)
        self.assertEqual(response.status_code, 200)

        # Convertir la réponse JSON en DataFrame et vérifier si elle est égale au DataFrame de référence
        response_data = json.loads(response.data)
        response_df = pd.DataFrame(response_data['df'])
        ref_df = pd.DataFrame(ref_data)
        return pd.testing.assert_frame_equal(response_df, ref_df)
    
    def process_testing_df_dfRejected(self, test_data_df, ref_data_dfRejected):
        # Envoyer une requête POST au point de terminaison /rules
        response = self.app.post(f'{SERVER_URL}/rules', json=test_data_df)

        # Vérifier si la réponse est un succès (code 200)
        self.assertEqual(response.status_code, 200)

        # Convertir la réponse JSON en DataFrame et vérifier si elle est égale au DataFrame de référence
        response_data = json.loads(response.data)
        response_dfRejected = pd.DataFrame(response_data['df_rejected'])
        ref_dfRejected = pd.DataFrame(ref_data_dfRejected)
        return pd.testing.assert_frame_equal(response_dfRejected, ref_dfRejected)
    
    def process_testing_both_df_dfRejected(self, test_data_df, ref_data_df, ref_data_dfRejected):
        # Envoyer une requête POST au point de terminaison /rules
        response = self.app.post(f'{SERVER_URL}/rules', json=test_data_df)

        # Vérifier si la réponse est un succès (code 200)
        self.assertEqual(response.status_code, 200)

        # Convertir la réponse JSON en DataFrame et vérifier si elle est égale au DataFrame de référence
        response_data = json.loads(response.data)
        response_df = pd.DataFrame(response_data['df'])
        ref_df = pd.DataFrame(ref_data_df)
        response_dfRejected = pd.DataFrame(response_data['df_rejected'])
        ref_dfRejected = pd.DataFrame(ref_data_dfRejected)
        return pd.testing.assert_frame_equal(response_df, ref_df) and pd.testing.assert_frame_equal(response_dfRejected, ref_dfRejected)

    def test_rules_endpoint_removes_duplicates(self):
        # Créer un DataFrame de test avec des duplicatas et le convertir en JSON
        test_data_df = [
            {'A': 1, 'B': 4},
            {'A': 2, 'B': 5},
            {'A': 2, 'B': 5},
            {'A': 3, 'B': 6},
        ]
        
        # Créer un DataFrame de référence sans duplicatas
        ref_data_df = [
            {'A': 1, 'B': 4},
            {'A': 2, 'B': 5},
            {'A': 3, 'B': 6},
        ]
        
        self.process_testing_only_df(test_data_df, ref_data_df)
        
    def test_rules_endpoint_removes_v_length(self):
        # Créer un DataFrame de test avec des duplicatas et le convertir en JSON
        test_data_df = [
            {'FathersName': 'A' * 101, 'FathersPreName': 'B', 'PatientNumber':1111},
            {'FathersName': 'A', 'FathersPreName': 'B' * 101, 'PatientNumber':5555},
            {'FathersName': 'D', 'FathersPreName': 'C', 'PatientNumber':6666},
        ]
        
        # Créer un DataFrame de référence sans duplicatas
        ref_data_df = [
            {'FathersName': 'A' * 101, 'FathersPreName': 'B', 'PatientNumber':1111},
            {'FathersName': 'A', 'FathersPreName': 'B' * 101, 'PatientNumber':5555},
            {'FathersName': 'D', 'FathersPreName': 'C', 'PatientNumber':6666},
        ]
        
        ref_data_dfRejected = [
            {'FathersName': 'A' * 101, 'PatientNumber':1111, 'Rule': 'V-length100' , 'Type' : 'warning', 'Message' : 'La longueur ne doit pas dépasser 100 caractères'},
            {'FathersPreName': 'B' * 101, 'PatientNumber':5555, 'Rule': 'V-length100' , 'Type' : 'warning', 'Message' : 'La longueur ne doit pas dépasser 100 caractères'},
        ]
        
        self.process_testing_both_df_dfRejected(test_data_df, ref_data_df, ref_data_dfRejected)

if __name__ == "__main__":
    unittest.main()