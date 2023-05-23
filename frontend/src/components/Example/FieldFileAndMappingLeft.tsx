
import { BsLayoutThreeColumns } from 'react-icons/bs';
import { DragDropContext, Droppable } from 'react-beautiful-dnd';

interface FieldFileAndMappingLeftProps {
  uploadedFileName: string | null;
  unmappedHeaders: string[];

  FieldMappingLeft: string[];
}

const FieldFileAndMappingLeft = ({ uploadedFileName, unmappedHeaders, FieldMappingLeft,
} : FieldFileAndMappingLeftProps) => {

  //Function 

  const onDragEnd = () => {
    console.log("Hello")
  }

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <div className="row">
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
          <button className="btn btn-danger">
            Clear File Columns
          </button>
        </div>
        <div className="col-lg-8 d-flex">
          <div className="col-sm-6 mb-3">
            <div className="table-responsive">
              {/* First Table */}
              <table className="table table-bordered caption-top">
                <caption className="pt-0 fw-semibold">Table de Mapping - Excel Input</caption>
                <thead className="table-dark">
                  <tr>
                    <th scope="col">Champ du fichier Excel Input</th>
                  </tr>
                </thead>
                <tbody id="tableau-element-input">
                  {FieldMappingLeft.map((index) => (
                    <tr key={index} className="border border-secondary">
                      <td>{"value"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
          <div className="col-sm-6 mb-3">
            <div className="table-responsive">
              {/* Second Table */}
              <table className="table table-bordered caption-top">
                <caption className="pt-0 fw-semibold">Table de Mapping - Mapper pour l'Output</caption>
                <thead className="table-dark">
                  <tr>
                    <th scope="col">Champ Possible à Mapper pour l'Output</th>
                  </tr>
                </thead>
                <tbody id="tableau-element-output">
                  {FieldMappingLeft.map((value, index) => (
                    <tr key={index} className="border border-secondary">
                      <td>{value}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </DragDropContext>
  );
};

export default FieldFileAndMappingLeft;
