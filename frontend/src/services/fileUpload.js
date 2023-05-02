const uploadFile = (file) => {  // Définition de la fonction uploadFile qui prend en paramètre un objet file (représentant le fichier sélectionné par l'utilisateur)
  const formData = new FormData(); // Création d'un nouvel objet FormData qui permet de stocker les données du formulaire

  formData.append('file', file); // Ajout du fichier dans le dictionnaire formData

  fetch('http://localhost:5000/upload', { // Envoi de la requête HTTP POST au serveur Flask situé à l'adresse http://localhost:5000/upload
    method: 'POST', // Spécification de la méthode HTTP POST
    body: formData // Ajout du dictionnaire formData comme corps de la requête
  })

  .then(response => { // Gestion de la réponse du serveur
    if (!response.ok) { // Si la réponse n'est pas 'ok' (code de statut HTTP 200)
      throw new Error('Network response was not ok'); // Lance une erreur avec un message d'erreur
    }
    return response.json(); // Retourne la réponse sous forme de JSON
  })
  .then(data => { // Traitement de la réponse JSON
    console.log('Upload successful'); // Affiche un message de confirmation dans la console du navigateur
  })
  .catch(error => { // Gestion des erreurs
    console.error('Error uploading file: ', error); // Affiche un message d'erreur dans la console du navigateur avec le message d'erreur spécifique
  });
}

  export default uploadFile;

/* Ceci est le code permettant au frontend d'envoyer le fichier au serveur afin qu'il le sauvegarde pour voir la fonctionnalité serveur il faut chercher le code commençant
avec app.route(/upload) du coté backend
*/
  