interface TableProps {
  data: string[];
}

function Table({ data }: TableProps) {
  return (
    <div className="col-sm-8 mb-3">
      <div className="table-responsive">
        <table className="table table-bordered caption-top">
          <caption className="pt-0 fw-semibold" >Table de Mapping</caption>
          <thead className="table-dark">
            <tr>
              <th scope="col">Champ du fichier Excel Input</th>
              <th scope="col">Champ Possible à Mapper pour l'Output</th>
            </tr>
          </thead>
          <tbody>
            {data.map((value, index) => (
              <tr key={index}>
                <td>{}</td>
                <td>{value}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Table;
