
import { BsLayoutThreeColumns } from 'react-icons/bs';


interface FileColumnsProps {
  uploadedFileName: string | null;
}

function FileColumns({ uploadedFileName}: FileColumnsProps) {

  return (
    <div className="list-group mb-3">
      <li className="list-group-item d-flex align-items-center justify-content-center gap-2 text-white bg-gradient-pink">
        <BsLayoutThreeColumns size="20" />
        <span className="fw-semibold">
          {uploadedFileName
            ? `${uploadedFileName} - File Columns`
            : 'File Columns'}
        </span>
      </li>
    </div>
  );
}

export default FileColumns;
