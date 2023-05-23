
import { BsLayoutThreeColumns } from 'react-icons/bs';


interface FieldFileAndMappingLeftProps {
  uploadedFileName: string | null;
  unmappedHeaders: string[];
}

const FieldFile = ({ uploadedFileName, unmappedHeaders,
} : FieldFileAndMappingLeftProps) => {


  return (
        <div className="col-lg-4 mt-3 pt-3">
          <div className="list-group mb-3" id="file-column">
            <li className="list-group-item d-flex align-items-center justify-content-center gap-2 text-white bg-gradient-pink">
              <BsLayoutThreeColumns size="20" />
              <span className="fw-semibold">
                {uploadedFileName
                  ? `${uploadedFileName} - File Columns`
                  : 'File Columns'}
              </span>
            </li>
            {unmappedHeaders.map((header) => (
              <td key={header}>{header}</td>
            ))}
          </div>
        </div>


  );
};

export default FieldFile;
