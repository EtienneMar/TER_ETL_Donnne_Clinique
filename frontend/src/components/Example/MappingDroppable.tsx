
interface FieldFileAndMappingLeftProps {
  FieldMappingLeft: string[];
}

const MappingOutput = ({ FieldMappingLeft,
} : FieldFileAndMappingLeftProps) => {
  return (
    
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
                    <tr key={index} id={index} className="border border-secondary">
                      <td>{"value"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
  );
};

export default MappingOutput;
