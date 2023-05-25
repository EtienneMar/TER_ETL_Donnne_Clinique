import React, { useState, useRef } from 'react';
import { BsLayoutThreeColumns } from 'react-icons/bs';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { Dispatch, SetStateAction } from 'react';

const DraggableHeader: React.FC<{ header: string | null, setHeader?: (header: string | null) => void }> = ({ header, setHeader }) => {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: 'header',
    item: { header },
    end: (item, monitor) => {
      const dropResult = monitor.getDropResult();
      if (item && dropResult && setHeader) {
        setHeader("Faite Glisser le Champ correspondant");
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
  index: number;
  onDrop: (index: number, header: string) => void;
  droppedItem: string | null;
  setDroppedItem: (item: string | null) => void;
}

const DroppableField: React.FC<DroppableFieldProps> = ({ index, onDrop, droppedItem, setDroppedItem }) => {
  interface Item {header: string;}
  const [{ isOver }, drop] = useDrop(() => ({
    accept: 'header',
    drop: (item: Item) => {
      onDrop(index, item.header);
      setDroppedItem(item.header);
    },
    collect: (monitor) => ({
      isOver: !!monitor.isOver(),
    }),
  }));

  return (
    <td
      ref={drop}
      style={{ backgroundColor: isOver ? 'lightgreen' : 'white' }}
    >
      {droppedItem && (
        <DraggableHeader header={droppedItem} setHeader={setDroppedItem} key={droppedItem}  />
      )}
    </td>
  );
};

interface FieldFileAndMappingLeftProps {
  uploadedFileName: string | null;
  unmappedHeaders: string[];
  FieldMappingLeft: string[];
  setunmappedHeader: Dispatch<SetStateAction<string[]>>;
}

const FieldFileAndMappingLeft: React.FC<FieldFileAndMappingLeftProps> = ({uploadedFileName,unmappedHeaders,FieldMappingLeft, setunmappedHeader,}) => {
  
  //Déclaration des tableaux modifiant le React Dom

  
  const [, setDroppedHeaders] = useState<string[]>([]); 

  //Tableau permettant de stocker la 1ere réponse serveur des unmappedsHeaders afin de pouvoir reset les éléments avec le boutton 
  const initialUnmappedHeadersRef = useRef(unmappedHeaders); 


  /*le tableau droppedItems stocke les éléments déposés (chaînes de caractères ou valeurs nulles)
    La longueur initiale est déterminée par FieldMappingLeft.length pour faire correspondre le nombre de case de 
    tableau-element-output avec tableau-element-input
    Chaque élément est initialisé avec la valeur "Faite Glisser le Champ correspondant" */
  const [droppedItems, setDroppedItems] = useState<(string | null)[]>(
    new Array(FieldMappingLeft.length).fill("Faite Glisser le Champ correspondant")
  );
  
  const handleDrop = (index: number, header: string) => {
    setunmappedHeader((prevHeaders) => prevHeaders.filter((h) => h !== header));
    setDroppedHeaders((prev) => {
      const newDropped = [...prev];
      if (
        unmappedHeaders.filter((h) => h !== prev[index]) &&
        prev[index] !== undefined
      ) {
        setunmappedHeader((prevUnmapped) => [...prevUnmapped, prev[index]]);
      }
      newDropped[index] = header;
      return newDropped;
    });
  };


  
  const handleReset = () => {
    setunmappedHeader(initialUnmappedHeadersRef.current);
    setDroppedItems(new Array(FieldMappingLeft.length).fill("Faite Glisser le Champ correspondant"));
  };

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
                  : "File Columns"}
              </span>
            </li>
            {unmappedHeaders.map((header) => (
              <DraggableHeader header={header} key={header} />
            ))}
          </div>
          <button className="btn btn-danger" onClick={handleReset}>
            Clear File Columns
          </button>
        </div>
        <div className="col-lg-8 d-flex">
          <div className="col-sm-6 mb-3">
            <div className="table-responsive">
              <table className="table table-bordered caption-top">
                <caption className="pt-0 fw-semibold">
                  Table de Mapping - Excel Input
                </caption>
                <thead className="table-dark">
                  <tr>
                    <th scope="col">Champ du fichier Excel Input</th>
                  </tr>
                </thead>
                <tbody id="tableau-element-input">
                  {FieldMappingLeft.map((_, index) => (
                    <tr className="border border-secondary">
                      <DroppableField
                        index={index}
                        onDrop={handleDrop}
                        droppedItem={droppedItems[index]}
                        setDroppedItem={(item) => {
                          setDroppedItems((items) => {
                            const newItems = [...items];
                            newItems[index] = item;
                            return newItems;
                          });
                        }}
                      />
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
          <div className="col-sm-6 mb-3">
            <div className="table-responsive">
              <table className="table table-bordered caption-top">
                <caption className="pt-0 fw-semibold">
                  Table de Mapping - Mapper pour l'Output
                </caption>
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
    </DndProvider>
  );
};

export default FieldFileAndMappingLeft;
