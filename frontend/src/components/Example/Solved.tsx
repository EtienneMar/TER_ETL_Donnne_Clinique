import React, { useState } from 'react';
import { BsLayoutThreeColumns } from 'react-icons/bs';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';



const DraggableHeader: React.FC<{ header: string | null, setHeader?: (header: string | null) => void }> = ({ header, setHeader }) => {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: 'header',
    item: { header },
    end: (item, monitor) => {
      const dropResult = monitor.getDropResult();
      console.log("dropResult : ", dropResult)
      console.log("Item : ", item)
      if (item && dropResult && setHeader) {
        setHeader("Faite Glisser le Champ correspondant"); // Reset the header value once it is dropped.
      }else {
        const fileColumn = document.getElementById('file-column');
        const elements = fileColumn?.getElementsByTagName('li');
        if (elements) {
          for (let i = 0; i < elements.length; i++) {
            if (elements[i].textContent === header) {
              elements[i].style.display = 'none';
              break;
            }
            }
        }
      }
    },
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
    canDrag: () => header !== "Faite Glisser le Champ correspondant"
  }));

  return (
    <div ref={drag} style={{ opacity: isDragging ? 0.5 : 1 }}>
      {header}
    </div>
  );
};


interface DroppableFieldProps {
  onDrop: (header: string) => void;
}

const DroppableField: React.FC<DroppableFieldProps>  = ({ onDrop  }) => {
  const [droppedItem, setDroppedItem] = useState<string | null>("Faite Glisser le Champ correspondant");

  const [{ isOver }, drop] = useDrop(() => ({
    accept: 'header',
    drop: (item) => {
      onDrop(item.header);
      setDroppedItem(item.header);
    },
    collect: (monitor) => ({
      isOver: !!monitor.isOver(),
    }),
  }));
  return (
    <td
      ref={drop}
      style={{
        backgroundColor: isOver ? 'lightgreen' : 'white',
      }}
    >
      {droppedItem && (
          <DraggableHeader header={droppedItem} setHeader={setDroppedItem} key={droppedItem} />
      )}
    </td>
  );
};

interface FieldFileAndMappingLeftProps {
  uploadedFileName: string | null;
  unmappedHeaders: string[];
  FieldMappingLeft: string[];

}

const FieldFileAndMappingLeft: React.FC<FieldFileAndMappingLeftProps> = ({
  uploadedFileName,
  unmappedHeaders,
  FieldMappingLeft,

}) => {

  const handleDrop = (header: string | null) => {
    //console.log('Handle Drop:', header);
    
    const fileColumn = document.getElementById('file-column');
    const elements = fileColumn?.getElementsByTagName('li');
    if (elements) {
      for (let i = 0; i < elements.length; i++) {
        if (elements[i].textContent === header) {
          elements[i].style.display = 'none';
          break;
        }
      }
    }
/*    const champFichierExcelInput = document.getElementById('tableau-element-input');
    const liElements = champFichierExcelInput?.getElementsByTagName('li');
    if (liElements) {
      for (let i = 0; i < liElements.length; i++) {
          if(liElements[i].textContent ===header) {
              liElements[i].textContent = "Faite Glisser le Champ correspondant"
          }
      }
    }    */   
  };

  const handleClearElements = () => {
    const fileColumn = document.getElementById('file-column');
    const elements = fileColumn?.getElementsByTagName('li');
    if (elements) {
      for (let i = 0; i < elements.length; i++) {
        if (elements[i].style.display == 'none') {
          elements[i].style.display = 'flex';
        }
      }
    }
  };
    /*const fileColumn = document.getElementById('file-column');
    const elements = fileColumn?.getElementsByTagName('li');
    if (elements) {
      for (let i = 0; i < elements.length; i++) {
        elements[i].style.display = 'block';
      }
    }*/
    return (
      <DndProvider backend={HTML5Backend}>
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
              {unmappedHeaders.map((header, index) => (
              <DraggableHeader header={header} key={index} />
            ))}
      </div>
            <button className="btn btn-danger" onClick={handleClearElements}>
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
                        <DroppableField onDrop={handleDrop}  />
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
                      <tr key={index}className="border border-secondary">
                        <td>{value}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </DndProvider>
    );      
};

export default FieldFileAndMappingLeft;


const handleDrop = (index: number, header: string) => {
  setunmappedHeader(prevHeaders => prevHeaders.filter(h => h !== header));
  setDroppedHeaders(prev => {
    const newDropped = [...prev];
    //console.log("New Dropped", newDropped)
    //console.log("New prev",prev[index])
    if (unmappedHeaders.filter(h => h !==prev[index])){
        setunmappedHeader(prevUnmapped => [...prevUnmapped, prev[index]!]);
    }
    newDropped[index] = header; // Mettre à jour le header à l'index spécifié
    return newDropped;
  });
};