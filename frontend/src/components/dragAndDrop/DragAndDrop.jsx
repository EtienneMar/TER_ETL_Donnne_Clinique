// Importe la bibliothèque React et la fonction useState depuis le package 'react'
import React, { useState } from 'react';
// Importe le fichier CSS associé à ce composant
import './DragAndDrop.css';
// Importe la fonction uploadFile depuis le fichier '../../services/fileUpload'
import uploadFile from '../../services/fileUpload';

// Déclaration du composant fonctionnel DragAndDrop
const DragAndDrop = () => {
  // Utilisation de l'état avec useState pour stocker le fichier sélectionné
  // et sa fonction de mise à jour setSelectedFile
  const [selectedFile, setSelectedFile] = useState(null);

  // Déclaration de la fonction handleDragStart pour gérer le début du glisser-déposer
  const handleDragStart = (ev) => {
    // Affiche "Started" dans la console du navigateur
    console.log("Started");
  }

  // Déclaration de la fonction handleDrag pour gérer le glissement de l'élément
  const handleDrag = (ev) => {
    // Affiche "Dragging" dans la console du navigateur
    console.log("Dragging")
  }

  // Déclaration de la fonction handleDragEnd pour gérer la fin du glisser-déposer
  const handleDragEnd = (ev) => {
    // Affiche "Ended" dans la console du navigateur
    console.log("Ended")
  }

  // Déclaration de la fonction handleDrop pour gérer le dépôt de l'élément dans la zone DragAndDrop
  const handleDrop = (ev) => {
    // Empêche l'événement par défaut du navigateur lors du dépôt
    ev.preventDefault();
    // Récupère le fichier déposé
    const file = ev.dataTransfer.files[0];
    // Vérifie si le fichier est un fichier Excel
    if (file && file.type !== 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') {
      // Affiche une alerte si le fichier n'est pas un fichier Excel
      alert('Le fichier déposé n\'est pas un fichier Excel.');
    } else {
      // Crée un nouvel objet FileReader pour lire le contenu du fichier
      const reader = new FileReader();
      // Lit le contenu du fichier en tant que URL de données
      reader.readAsDataURL(file);
      // Met à jour l'état selectedFile avec le fichier déposé
      setSelectedFile(file);
    }
  }

  // Déclaration de la fonction handleDragOver pour gérer le survol de l'élément
  const handleDragOver = (ev) => {
    // Empêche l'événement par défaut du navigateur lors du survol
    ev.preventDefault();
  }

  // Déclaration de la fonction handleChange pour gérer le changement de l'input pour sélectionner un fichier
  const handleChange = (event) => {
    const file = event.target.files[0]; // Récupère le fichier sélectionné
    
    // Vérifie si le fichier est un fichier Excel
    if (file && file.type !== 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' ) {
      alert('Le fichier sélectionné n\'est pas un fichier Excel.'); // Affiche une alerte si le fichier n'est pas un fichier Excel
    } else {
      setSelectedFile(file); // Met à jour l'état selectedFile avec le fichier sélectionné
    }
  }

  // Déclaration de la fonction handleUpload pour gérer l'envoi du fichier sélectionné
  const handleUpload = () => {
    if (selectedFile) { // Vérifie si un fichier a été sélectionné
      uploadFile(selectedFile); // Appelle la fonction uploadFile pour envoyer le fichier sélectionné
    } else {
      alert('Veuillez sélectionner un fichier avant de l\'uploader.'); // Affiche une alerte si aucun fichier n'a été sélectionné
    }
  }
  
  // Retourne le JSX du composant à afficher
  return (
  <div className="Drop_file_and_input_file">
  <div
       className='Drag_And_Drop'
       onDragStart={handleDragStart}
       onDrag={handleDrag}
       onDragEnd={handleDragEnd}
       onDrop={handleDrop}
       onDragOver={handleDragOver}
     ></div>
  <input className='inputFile' type="file" id="myFile" onChange={handleChange} />
  <button type="button" onClick={() => document.getElementById('myFile').click()}>Browse</button>
  <button id="uploadButton" onClick={handleUpload}>Upload</button>
  <p id="status">{selectedFile ? selectedFile.name : 'No file selected'}</p>
  </div>
  );
  }
  
  // Exporte le composant DragAndDrop par défaut pour être utilisé dans d'autres modules
  export default DragAndDrop;