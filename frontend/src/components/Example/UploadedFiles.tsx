import { BsListUl, BsFileEarmarkExcel } from 'react-icons/bs';

interface UploadedFilesProps {
  uploadedFile: File | null;
  uploadedFileName: string | null; // Ajout de la propriété uploadedFileName
}

function UploadedFiles({ uploadedFile, uploadedFileName }: UploadedFilesProps) {
  return (
    <div className="list-group mb-3">
      <li className="list-group-item d-flex align-items-center justify-content-center gap-2 text-white bg-gradient-success">
        <BsListUl size="20" />
        <span className="text-capitalize fw-semibold">
          Latest Uploaded Excel File
        </span>
      </li>
      {uploadedFile && uploadedFileName && (
        <button
          type="button"
          className="list-group-item list-group-item-action d-flex align-items-center gap-2"
        >
          <BsFileEarmarkExcel size="20" />
          <span>{uploadedFileName}</span>
        </button>
      )}
    </div>
  );
}

export default UploadedFiles;
