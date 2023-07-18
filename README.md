# TER_ETL_Donnne_Clinique

Stack à avoir sur son ordinateur : 
- Vite.JS
- Node avec React d'installer
- Python 3
- Docker

Afin de pouvoir utiliser cette application il est nécessaire d'avoir au préalable Docker, un logiciel de base de données style MySQL et surtout mettre à jour les adresses ip de la base de donnée dans le code celle-ci est utilisée pour service header comme suivant :

def connect_to_database():
    db = mysql.connector.connect(
        host='host.docker.internal',
        port=3307,
        user='root',
        password='root',
        database='ter'
    )

Étape  1 : Récupérer le script d'initialisation de la base de donnée {db} dans scripting db.
Étape 2 : Se placer dans le répertoire du projet où se trouve le docker compose et lancer un build afin de créer les images puis un up pour lancer l'ensemble du projet.

    docker compose build
    docker compose up 

Étape 3 : A noter pour faire fonctionner uniquement l'IHM notamment le drag and drop il faut avoir la base de donnée et le webservice header à minima d'activée 
Pour faire fonctionner l'IHM produisant le rapport il faut en plus du processus précédent activée le service de rapport
Pour faire fonctionner l'IHM d'inscription il faut le webService d'inscription et la BD activée