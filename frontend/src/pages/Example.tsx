import { useContext, useState } from 'react';
import { UserContext } from '../components/Global/UserProvider';
import { Hero } from '../components/Hero';
import { UploadedFiles, Dropdown, FieldFile, DropdownFileType, MappingOutput, MappingDroppable } from '../components/Example';

function Example() {
  const userContext = useContext(UserContext);
  if (!userContext) {
    throw new Error("useContext(UserContext) is null, did you forget a UserProvider?");
  }
  const { uploadedFiles, currentFile } = userContext;
  const lastUploadedFile = uploadedFiles[uploadedFiles.length - 1];
  const [unmappedHeaders, setUnmappedHeaders] = useState<string[]>([]);
  const [mapped_table_remaining_possibility, setMappedTableRemainingPossibility] = useState<string[]>([]);

  const handleFileTypeSelect = (fileTypeName: string) => {
    // Gestion de l'appel serveur
    const formData = new FormData();
    formData.append('type_fichier', fileTypeName);
    if (currentFile !== null) {
      formData.append('file', currentFile);
    }

    fetch('http://localhost:5006/mapping_header', {
      method: 'POST',
      body: formData
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
      .then(data => {
        console.log('Upload successful', data);
        if (data.unmapped_headers) {
          setUnmappedHeaders(data.unmapped_headers);
        }
        if (data.mapped_table_remaining_possibility) {
          setMappedTableRemainingPossibility(data.mapped_table_remaining_possibility);
        }
      })
      .catch(error => {
        console.error('Error uploading file: ', error);
      });
  };

  return (
    <>
      <Hero
        title="Example Page 😁"
        content="An About page is a special web page on a site where your readers/visitors learn more about you and what you do."
      />
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
          <div className="row">
            {currentFile && (
              <FieldFile
                uploadedFileName={currentFile.name}
                unmappedHeaders={unmappedHeaders}
              />
            )}
            <div className="col-lg-8 d-flex">
              {currentFile && Object.keys(mapped_table_remaining_possibility).length > 0 &&(
                <><MappingDroppable
                    FieldMappingLeft={Object.values(mapped_table_remaining_possibility)} /><MappingOutput
                      FieldMappingLeft={Object.values(mapped_table_remaining_possibility)} /></>
                )}
            </div>
          </div>
        </div>
      </section>
    </>
  );
}

export default Example;
