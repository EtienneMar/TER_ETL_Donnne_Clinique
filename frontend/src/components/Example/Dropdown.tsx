import { useState, useEffect, useContext } from 'react';
import { BsFileEarmarkExcel } from 'react-icons/bs';
import { UserContext } from '../Global/UserProvider';

function Dropdown() {


  const userContext = useContext(UserContext);
  if (!userContext) {
      throw new Error("useContext(UserContext) is null, did you forget a UserProvider?");
  }
  const { uploadedFiles } = userContext;

  const [fileNames, setFileNames] = useState<string[]>([]);
  const [showWarning, setShowWarning] = useState(false); // Variable d'état pour le message d'avertissement

  useEffect(() => {
    if (uploadedFiles.length > 0) {
      const newFileNames = uploadedFiles.map(file => file.name);
      setFileNames(newFileNames);
      localStorage.setItem('uploadedFileNames', JSON.stringify(newFileNames));
    }
  }, [uploadedFiles]);

  useEffect(() => {
    if (fileNames.length === 0) {
      // Afficher un message d'avertissement s'il n'y a pas d'anciens fichiers Excel téléchargés
      setShowWarning(true);
    } else {
      setShowWarning(false);
    }
  }, [fileNames]);

  return (
    <div className="dropdown">
      <button
        className="btn btn-primary dropdown-toggle"
        type="button"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        Older Excel Files
      </button>
      {showWarning ? ( // Affiche le message d'avertissement en fonction de la variable d'état
        <ul className="dropdown-menu py-0">
          <li className="alert alert-warning mb-0" role="alert">
            There are no older uploaded Excel files to show.
          </li>
        </ul>
      ) : (
        <ul className="dropdown-menu">
          {fileNames.map((fileName, index) => (
            <li key={index}>
              <a
                href="#"
                className="dropdown-item d-flex align-items-center gap-2"
              >
                <BsFileEarmarkExcel size="20" />
                <span>{fileName}</span>
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Dropdown;
