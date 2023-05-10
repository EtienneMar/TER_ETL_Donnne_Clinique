FROM python:3.11.3



# Créer un répertoire pour le code source de l'application
WORKDIR /app

# Copier les fichiers de configuration et d'exigences
COPY requirements.txt ./

# Installez les paquets nécessaires spécifiés dans requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel le service sera accessible
EXPOSE 5002

ENV PYTHONPATH "${PYTHONPATH}:/app/application"

# Définir la commande à exécuter lors de l'exécution d'un conteneur basé sur cette image
ENTRYPOINT ["python", "/app/application/app.py"]
