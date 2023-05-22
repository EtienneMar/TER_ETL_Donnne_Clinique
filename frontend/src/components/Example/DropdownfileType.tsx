import { useState } from 'react';
import { BsFileEarmarkExcel } from 'react-icons/bs';

function DropdownFileType() {
  const fileType: Record<string, string> = {
    diagnosis: "Diagnosis",
    encounter: "Encounter",
    patient: "Patient",
    procedure: "Procedure",
    service: "Service",
  };

  const [selectedFileType, setSelectedFileType] = useState<string>();

  const handleFileTypeSelect = (fileName: string) => {
    setSelectedFileType(fileName);
  };

  const filteredFileTypes = Object.keys(fileType).filter(fileName => fileName !== selectedFileType);

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
        {filteredFileTypes.map((fileName, index) => (
          <li key={index}>
            <a
              href="#"
              className="dropdown-item d-flex align-items-center gap-2"
              onClick={() => handleFileTypeSelect(fileName)}
            >
              <BsFileEarmarkExcel size="20" />
              <span>{fileType[fileName]}</span>
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DropdownFileType;
