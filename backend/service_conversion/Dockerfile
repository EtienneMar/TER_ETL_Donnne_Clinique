FROM python:3.11.3

# Créer un répertoire pour le code source de l'application
WORKDIR /app

# Copier les fichiers de configuration et d'exigences
COPY requirements.txt ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel le service sera accessible
EXPOSE 5001

# Définir la commande à exécuter lors de l'exécution d'un conteneur basé sur cette image
ENTRYPOINT ["python", "/app/app.py"]
