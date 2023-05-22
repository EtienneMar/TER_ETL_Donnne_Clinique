import { useState, useContext } from 'react';
import { BsFileEarmarkExcel } from 'react-icons/bs';
import { UserContext } from '../Global/UserProvider';

function DropdownFileType() {
  const userContext = useContext(UserContext);
  if (!userContext) {
    throw new Error("useContext(UserContext) is null, did you forget a UserProvider?");
  }
  const { currentFile } = userContext;
  
  const fileType: Record<string, string> = {
    diagnosis: "Diagnosis",
    encounter: "Encounter",
    patient: "Patient",
    procedure: "Procedure",
    service: "Service",
  };

  const [selectedFileType, setSelectedFileType] = useState<string>();

  const handleFileTypeSelect = (fileTypeName: string) => {
    setSelectedFileType(fileTypeName);

    //Gestion de l'appel serveur 
    const formData = new FormData(); // Création d'un nouvel objet FormData qui permet de stocker les données du formulaire

    formData.append('type_fichier', fileTypeName); // Ajout du type du fichier dans le dictionnaire formData
    if (currentFile !== null) {
      formData.append('file', currentFile);
    }

    fetch('http://localhost:5006/testing_header', { // Envoi de la requête HTTP POST au serveur Flask situé à l'adresse http://localhost:5000/upload
      method: 'POST', // Spécification de la méthode HTTP POST
      body: formData // Ajout du dictionnaire formData comme corps de la requête
    })
    .then(response => {
      if (!response.ok) {
        console.error('Response status:', response.status, 'Status text:', response.statusText);
        return response.text().then(text => {
          throw new Error(text || 'Network response was not ok');
        });
      }
      return response.json();
    })
    .then(data => { // Traitement de la réponse JSON
      console.log('Upload successful', data); // Affiche un message de confirmation dans la console du navigateur
      
    })
    .catch(error => { // Gestion des erreurs
      console.error('Error uploading file: ', error); // Affiche un message d'erreur dans la console du navigateur avec le message d'erreur spécifique
    });
  };

  const filteredFileTypes = Object.keys(fileType).filter(fileType => fileType !== selectedFileType);

  return (
    <div className="dropdown">
      <span className="text-primary fw-bold">Type Fichier : </span>
      <button
        className="btn btn-primary dropdown-toggle"
        type="button"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        {selectedFileType ? fileType[selectedFileType] : "File Type"}
      </button>
      <ul className="dropdown-menu">
        {filteredFileTypes.map((fileTypeName, index) => (
          <li key={index}>
            <a
              href="#"
              className="dropdown-item d-flex align-items-center gap-2"
              onClick={() => handleFileTypeSelect(fileTypeName)}
            >
              <BsFileEarmarkExcel size="20" />
              <span>{fileType[fileTypeName]}</span>
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DropdownFileType;
