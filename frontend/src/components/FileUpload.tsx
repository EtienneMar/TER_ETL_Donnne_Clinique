import { BsCloudUpload } from 'react-icons/bs';
import { useState } from 'react';

function FileUpload() {
  const [selectedFile, setSelectedFile] = useState<File | null>();
  const [fileUrl, setFileUrl] = useState<string | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      const file = event.target.files[0];
      setSelectedFile(file);
      setFileUrl(URL.createObjectURL(file));
    }
  };

  const handleUploadClick = (file:File) => {
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
   

  return (
    <section className="py-5 bg-body-secondary">
      <div className="container py-5">
        <div className="col-lg-6 mx-auto">
          <h5 className="form-label mb-3">Upload Your File </h5>
          <div className="input-group">
            <input
              type="file"
              id="uploadFile"
              className="form-control"
              onChange={handleFileChange}
            />
            <button
              type="button"
              id="uploadFile"
              className="btn btn-primary d-inline-flex align-items-center justify-content-center gap-2"
              /* In this updated code, the handleUploadClick function will only be called if selectedFile is truthy 
              (i.e., not null or undefined). This check ensures that you're only passing a valid File object to the function, 
              resolving the type error.*/
              onClick={() => {
                if (selectedFile) {
                  handleUploadClick(selectedFile);
                }
              }}
              disabled={!selectedFile}
            >
              <BsCloudUpload size="20" />
              <span className="text-capitalize">Upload Now </span>
            </button>
          </div>
          {fileUrl && (
            <div className="mt-3">
              <img src={fileUrl} alt="Selected file" className="img-thumbnail" />
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

export default FileUpload;
