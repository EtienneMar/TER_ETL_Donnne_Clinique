import json
import sys
import pandas as pd
import numpy as np
from convertdate import islamic
from dateutil.parser import parse, ParserError
from datetime import datetime

def convert_date(date):
    date_string = date.strftime("%Y-%m-%d %H:%M:%S")
    hijri_year = islamic.from_gregorian(datetime.now().year, datetime.now().month, datetime.now().day)[0]
    if len(date_string) >= 10:
        try:
            dt = parse(date_string)
            if dt.year <= hijri_year :
                date_convertie = islamic.to_gregorian(dt.year, dt.month, dt.day)
                date_convertie = dt.replace(year=date_convertie[0], month=date_convertie[1], day=date_convertie[2])
                return date_convertie.strftime("%Y-%m-%d %H:%M:%S")
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except ParserError:
            pass
    else : 
        return date_string


if __name__ == '__main__':
    json_data = json.load(sys.stdin)
    file = json_data.get("FichierPatient")
    df = pd.DataFrame(file)
    columns = ["DATEOFBIRTH", "DATEOFDEATH"]
    for col in columns : 
        df[col] = pd.to_datetime(df[col])
        df[col] = df[col].apply(convert_date) 
    rapport_conformite = json_data.get("RapportConformite")
    output_data = {
        "FichierPatient": df.to_dict(orient="records"),
        "RapportConformite": rapport_conformite
    }
    json_output = json.dumps(output_data, ensure_ascii=False)

    # Afficher le JSON en sortie
    sys.stdout.write(json_output)
        