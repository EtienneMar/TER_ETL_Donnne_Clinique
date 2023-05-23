
interface FieldFileAndMappingLeftProps {
  FieldMappingLeft: string[];
}

const MappingOutput = ({ FieldMappingLeft,
} : FieldFileAndMappingLeftProps) => {

  //Function 


  return (
    
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
  );
};

export default MappingOutput;
