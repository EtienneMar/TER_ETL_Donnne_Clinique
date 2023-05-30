import { BsCloudUpload } from 'react-icons/bs';
import { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { UserContext } from '../Global/UserProvider';

function FileUpload() {

  //Déclaration des tableaux
  const [selectedFile, setSelectedFile] = useState<File | null>();
  const [showFileTypeAlert, setShowFileTypeAlert] = useState(false);
  const [showFileExistsAlert, setShowFileExistsAlert] = useState(false);
  const navigate = useNavigate();

  //Contexte Utilisateur pour stocker le fichier
  const userContext = useContext(UserContext);
  if (!userContext) {
    throw new Error("useContext(UserContext) is null, did you forget a UserProvider?");
  }
  const { uploadedFiles, setUploadedFiles } = userContext;

  //Gestion du changement des fichiers : Extension du fichier  
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      const file = event.target.files[0];
      if (file && file.type !== 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') {
        // Affiche une alerte si le fichier n'est pas un fichier Excel
        setShowFileTypeAlert(true);
        setShowFileExistsAlert(false)
        setSelectedFile(null);
      } else {
        setShowFileTypeAlert(false);
        setSelectedFile(file);
      }
    }
  };

  //Gestion du changement des fichiers : Dépôt du fichier et Test Fichiers existants  
  const handleUploadClick = (file: File) => {
    const isFileAlreadyUploaded = uploadedFiles.some(
      (uploadedFile: File) => uploadedFile.name === file.name
    );
    if (isFileAlreadyUploaded) {
      setShowFileTypeAlert(false)
      setShowFileExistsAlert(true);
      return;
    }
    setUploadedFiles((prevUploadedFiles: File[]) => [...prevUploadedFiles, file]);
    navigate('/mapping');
  };

  return (
    <section className="py-5 bg-body-secondary">
      <div className="container py-5">
        <div className="col-lg-6 mx-auto">
          <h5 className="form-label mb-3">Upload Your File </h5>
          {showFileTypeAlert && (
            <div className="alert alert-danger mt-3" role="alert">
              Le fichier déposé n'est pas un fichier <strong>Excel</strong>.
            </div>
          )}
          {showFileExistsAlert && (
            <div className="alert alert-danger mt-3" role="alert">
              Le fichier <strong>{selectedFile?.name}</strong> est déjà déposé.
            </div>
          )}
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
        </div>
      </div>
    </section>
  );
}

export default FileUpload;
