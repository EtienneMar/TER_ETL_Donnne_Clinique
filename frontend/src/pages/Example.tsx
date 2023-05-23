import { useContext, useState, /*useEffect*/ } from 'react';
import { UserContext } from '../components/Global/UserProvider';
import { Hero } from '../components/Hero';
import {UploadedFiles, Dropdown, DropdownFileType, FieldFileAndMappingLeft} from '../components/Example';

function Example() {
  const userContext = useContext(UserContext);
  if (!userContext) {
      throw new Error("useContext(UserContext) is null, did you forget a UserProvider?");
  }
  const { uploadedFiles, currentFile } = userContext;
  const lastUploadedFile = uploadedFiles[uploadedFiles.length - 1]
  const [unmappedHeaders, setUnmappedHeaders] = useState<string[]>([]);
  const [mapped_table_remaining_possibility, setMappedTableRemainingPossibility] = useState<string[]>([]);

  const handleFileTypeSelect = (fileTypeName : string) => {
    //Gestion de l'appel serveur 
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
      }
      if (data.mapped_table_remaining_possibility) {
        setMappedTableRemainingPossibility(data.mapped_table_remaining_possibility);
      }
    })
    .catch(error => { // Gestion des erreurs
      console.error('Error uploading file: ', error); // Affiche un message d'erreur dans la console du navigateur avec le message d'erreur spécifique
    });
  };
/*
              <FileColumns
                uploadedFileName={uploadedFileName}
                uploadedFile={uploadedFile}
              />
                            <Table />
*/
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
          <div className="col-4">
            <DropdownFileType onFileTypeSelect={handleFileTypeSelect} />
          </div>
        </div>
            {currentFile && Object.keys(mapped_table_remaining_possibility).length > 0 &&(
              <FieldFileAndMappingLeft
                uploadedFileName={currentFile.name}
                unmappedHeaders={unmappedHeaders}
                FieldMappingLeft={Object.values(mapped_table_remaining_possibility)}
              />
            )}
      </div>
    </section>
  </>
);
}

export default Example;