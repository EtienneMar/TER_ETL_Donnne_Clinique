# Importation des bibliothèques nécessaires
import json, os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

# Définition du dossier d'upload et des extensions de fichiers autorisées
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

# Crée le dossier d'upload s'il n'existe pas
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialisation de l'application Flask et activation des CORS
app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route pour la page d'accueil
@app.route('/')
def index():
    # Crée une chaîne JSON et la parse en objet Python
    json_string = '{"message" : "HelloWorld"}'
    parsed_data = json.loads(json_string)
    # Retourne l'objet Python sous forme de réponse JSON
    return parsed_data

# Fonction pour vérifier si le fichier a une extension autorisée
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route pour gérer l'upload de fichiers
@app.route('/upload', methods=['POST'])
def upload_file():
    # Vérifie si la requête contient un fichier
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    # Vérifie si un fichier a été sélectionné
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    # Vérifie si le fichier est autorisé et le sauvegarde
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"message": "Upload successful"}), 200
    else:
        return jsonify({"error": "File not allowed"}), 400

# Exécute l'application Flask en mode debug et sur toutes les adresses IP disponibles
if __name__ == '__app__':
    app.run(debug=True, host='0.0.0.0')
