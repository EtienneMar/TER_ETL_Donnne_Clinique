import { useState, useContext } from 'react';
import { BsFileEarmarkExcel } from 'react-icons/bs';
import { UserContext } from '../Global/UserProvider';

interface DropdownFileTypeProps {
  onFileTypeSelect: (fileTypeName: string) => void;
}

const DropdownFileType: React.FC<DropdownFileTypeProps> = ({ onFileTypeSelect }) => {
  const userContext = useContext(UserContext);
  if (!userContext) {
    throw new Error("useContext(UserContext) is null, did you forget a UserProvider?");
  }

  
  const fileType: Record<string, string> = {
    Diagnosis: "Diagnosis",
    Encounter: "Encounter",
    Patient: "Patient",
    Procedure: "Procedure",
    Service: "Service",
    Transfer : "Transfer"
  };

  const [selectedFileType, setSelectedFileType] = useState<string>();

  const handleFileTypeSelect = (fileTypeName: string) => {
    setSelectedFileType(fileTypeName);
    onFileTypeSelect(fileTypeName);
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
