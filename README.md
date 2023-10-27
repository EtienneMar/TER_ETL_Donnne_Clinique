# TER_ETL_Donnne_Clinique


Le dossier backend contient tout les services de l'appication en FLASK
Le dossier frontend contient la vue de l'application
Le dossier nifi contient les scripts insérer dans nifi à travers docker
Le dossier ressource contient le script SQL pour la base de donnée, les diapositives du TER, le rapport etc...

Chaque service contient son propre dockerfile

Pour développer sur le projet les stack à avoir sur son ordinateur :

- Node JS, React
- Python 3 avec les Bibliothèqes suivante
  - Flask, Flask_Cors
  - Pandas
  - Numpy
  - io
  - openpyxl
  - werkzeug.security
  - urllib3
  - http.cookies
  - Docker
  - Base de donnée MYSQL, Attention le script d'instanciation de la base de données ne fonctionne pas avec PostGres



Étape  1 : Récupérer le script d'initialisation de la base de donnée {db} dans scripting db.
Étape 2 : Se placer dans le répertoire du projet où se trouve le docker compose et lancer un build afin de créer les images puis un up pour lancer l'ensemble du projet.
    
    Démarrer le daemon docker
    docker compose create

    Changer les adresse de la base de données
    Créer votre utilisateur de base de donnée
    Créer une base TER

    docker compose build
    docker compose up pour lancer tout les conteneurs dans un terminal 
    docker compose up nifi, conversion etc... pour lancer les services un à un

Étape 3 : A noter pour faire fonctionner uniquement l'IHM notamment le drag and drop il faut avoir la base de donnée et le webservice header à minima d'activée 
Pour faire fonctionner l'IHM produisant le rapport il faut en plus du processus précédent activée le service de rapport
Pour faire fonctionner l'IHM d'inscription il faut le webService d'inscription et la BD activée