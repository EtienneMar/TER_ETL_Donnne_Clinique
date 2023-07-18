import { useContext,  useState } from 'react';
import { UserContext } from '../components/Global/UserProvider';
import { Hero } from '../components/Hero';
import {UploadedFiles, Dropdown, DropdownFileType, FieldFileAndMappingLeft} from '../components/Mapping';

function Mapping() {
  const userContext = useContext(UserContext);
  if (!userContext) {
      throw new Error("useContext(UserContext) is null, did you forget a UserProvider?");
  }
  const { uploadedFiles, currentFile } = userContext;
  const lastUploadedFile = uploadedFiles[uploadedFiles.length - 1]
  const [unmappedHeaders, setUnmappedHeaders] = useState<string[]>([]);
  const [mapped_table_remaining_possibility, setMappedTableRemainingPossibility] = useState<string[]>([]);
  const [initialUnmappedHeadersRef, setinitialUnmappedHeadersRef] = useState<string[]>([]);
  const [mappedHeaders, setMappedHeader] = useState<Record<string, string>>({});
  const [selectedFileType, setSelectedFileType] = useState<string>()
  
  /*le tableau droppedItems stocke les éléments déposés (chaînes de caractères ou valeurs nulles)
    La longueur initiale est déterminée par FieldMappingLeft.length pour faire correspondre le nombre de case de 
    tableau-element-output avec tableau-element-input
    Chaque élément est initialisé avec la valeur "Faite Glisser le Champ correspondant" */
  const [droppedItems, setDroppedItems] = useState<(string)[]>([]);

  const handleFileTypeSelect = (fileTypeName : string) => {
    setSelectedFileType(fileTypeName)
    const formData = new FormData(); // Création d'un nouvel objet FormData qui permet de stocker les données du formulaire
    formData.append('type_fichier', fileTypeName); // Ajout du type du fichier dans le dictionnaire formData
    if (currentFile !== null) {
      formData.append('file', currentFile);
    }

    fetch('http://localhost:5006/mapping_header', { // Envoi de la requête HTTP POST au serveur Flask situé à l'adresse http://localhost:5000/upload
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
      if (data.unmapped_headers) {
        setUnmappedHeaders(data.unmapped_headers);
        setinitialUnmappedHeadersRef(data.unmapped_headers);
      }
      if (data.mapped_table_remaining_possibility) {
        setMappedTableRemainingPossibility(data.mapped_table_remaining_possibility);
      }
      if (data.mapped_headers && Object.keys(data.mapped_headers).length !== 0) {
        setMappedHeader(data.mapped_headers)
      }
    })
    .catch(error => { // Gestion des erreurs
      console.error('Error uploading file: ', error); // Affiche un message d'erreur dans la console du navigateur avec le message d'erreur spécifique
    });
  };

  //Ici on envoie le mapping du fichier et le fichier afin de traiter la donnée
  const handleUploadForTreatment = (file: File, selectedFileType : string) =>{
    //Gestion de l'appel serveur 
    const formData = new FormData(); // Création d'un nouvel objet FormData qui permet de stocker les données du formulaire
    formData.append('type_fichier', selectedFileType); 
    console.log(file);
    //formData.append('file', file); // Ajout du fichier dans le dictionnaire formData
    formData.append('nom_fichier', file.name)
    const mapping: { [key: string]: string } = {...mappedHeaders}; //Récupération des mappedsHeaders déjà existants.

    droppedItems.forEach(element => {//Ajout des mappings Userss
      if (element !== "Faite Glisser le Champ correspondant") {
        console.log("IndexOf", mapped_table_remaining_possibility)
        console.log("un" , unmappedHeaders)
        mapping[element] = mapped_table_remaining_possibility[droppedItems.indexOf(element)]
      }
    });
    console.log("MAPPING",mapping)
    formData.append('mapping', JSON.stringify(mapping))

    fetch('http://localhost:5006/check_header', { // Envoi de la requête HTTP POST au serveur Flask situé à l'adresse http://localhost:5000/upload
      method: 'POST', // Spécification de la méthode HTTP POST
      body: formData // Ajout du dictionnaire formData comme corps de la requête
    })
  
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      // Vérifiez si la réponse a le type de contenu application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
      if (response.headers.get("content-type") === "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") {
        return response.blob(); // Retournez la réponse comme un blob
      } else {
        return response.json(); // Sinon, retournez la réponse comme JSON
      }
    })
    .then(data => {
      if (data instanceof Blob) {
        const url = window.URL.createObjectURL(data); // Créez une URL d'objet pour le blob
        const a = document.createElement('a'); // Créez une nouvelle ancre
        a.href = url; // Définissez l'URL de l'ancre sur l'URL de l'objet
        a.download = 'rapport_mandatory_fields.xlsx'; // Définissez le nom du fichier à télécharger
        document.body.appendChild(a); // Ajoutez l'ancre à l'élément body du document
        a.click(); // Cliquez sur l'ancre pour déclencher le téléchargement
        a.remove(); // Retirez l'ancre de l'élément body du document
      } else {
        
        if (data.value === true) {
         formData.append('file', file)
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
         console.log('Upload successful', data); // Affiche un message de confirmation dans la console du navigateur
       })
       .catch(error => { // Gestion des erreurs
         console.error('Error uploading file: ', error); // Affiche un message d'erreur dans la console du navigateur avec le message d'erreur spécifique
       });
      }
    }
    })
    .catch(error => {
      console.error('Error uploading file: ', error);
    });
  };
return (
  <>
    <Hero title="Example Page 😁"
      content="An About page is a special web page on a site where your readers/visitors learn more about you and what you do."
    ></Hero>
    <section className="py-5 bg-body-secondary">
      <div className="container py-5">
        <div className="row p-0">
          <div className="col-lg-4">
            {lastUploadedFile && (
              <UploadedFiles
                uploadedFile={lastUploadedFile}
                uploadedFileName={lastUploadedFile.name}
              />
            )}
            
          </div>
          <div className="col-4">
            <Dropdown />
          </div>
          <div className="col-4" id="file_name">
            <DropdownFileType onFileTypeSelect={handleFileTypeSelect}/>
          </div>
        </div>
        <div className="row">
        <div >
         {/*Rajouter un truc pour empecher d'afficher le bouton tant que DroppedItem est nul*/} 
        <button
        className="btn btn-success "
        type="submit"
        aria-expanded="false"
        onClick={() => {
          if (currentFile && selectedFileType !== undefined) {
            handleUploadForTreatment(currentFile, selectedFileType);
          }
        }}
      >Upload for Treatment 
      </button>
      </div>
            {currentFile && Object.keys(mapped_table_remaining_possibility).length > 0 &&(
              <FieldFileAndMappingLeft
                uploadedFileName={currentFile.name}
                unmappedHeaders={unmappedHeaders}
                setunmappedHeader={setUnmappedHeaders}
                FieldMappingLeft={Object.values(mapped_table_remaining_possibility)}
                droppedItems={droppedItems}
                setDroppedItems={setDroppedItems}
                initialUnmappedHeadersRef={initialUnmappedHeadersRef}
              />
            )}
      </div>
      </div>


    </section>
  </>
);
}

export default Mapping;