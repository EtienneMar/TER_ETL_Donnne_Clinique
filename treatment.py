import sys
import json
import pandas as pd
from treatmentData import hijri_and_removeLeadingZero, lenght_and_character_Columns, NotNull
import simplejson 

def remove_duplicate_rows(df, df1):
    # obtenir les index des lignes à supprimer
    rows_to_remove = df[df.isin(df1.to_dict(orient='list')).all(axis=1)].index
    # supprimer les lignes
    df = df.drop(rows_to_remove)    
    return df


# Read the FlowFile content from standard input
flowfile_content = sys.stdin.read()

# Load the JSON data
data = json.loads(flowfile_content)

# Transform the data into a DataFrame
df = pd.json_normalize(data)

rejected_fathers_name = lenght_and_character_Columns(df, "FathersName", 100, lenghtColumns=True, alphaCharacter=True, typeRule_AlphaCharacter='warn')
rejected_fathers_prename = (lenght_and_character_Columns(df, "FathersPreName", 100, lenghtColumns=True, alphaCharacter=True, typeRule_AlphaCharacter='warn'))
rejected_place_of_birth = (lenght_and_character_Columns(df, "PlaceOfBirth", 100, lenghtColumns=True))
rejected_hospital = (NotNull(df, "Hospital"))

rejected = rejected_fathers_name.merge(rejected_fathers_prename, how='outer').merge(rejected_place_of_birth, how='outer').merge(rejected_hospital, how='outer')

#There is no SourcePatientNumber in the mapping give by Bilel I get an error while I turn on this value
#rejected.merge(lenghtColumns(df, "SourcePatientNumber", 50, lenghtColumns=True))
dfList = hijri_and_removeLeadingZero(df, date=True, removeLeadingZero=True)

df = (dfList[0]) 
rejected = rejected.merge(dfList[1], how='outer')

if 'rejected'  in rejected['Type'].values:
    # merge the type column from the rejected dataframe with the original dataframe based on the index
    merged_df = pd.merge(df, rejected[['Type']], how='left', left_index=True, right_index=True)

    # create a boolean mask to identify the rows to be removed
    mask = (merged_df['Type'] == 'rejected')

    # drop the rows from the original dataframe
    clean_df = df.drop(merged_df[mask].index)
    records = clean_df.to_dict(orient='records')
else : 
    records = df.to_dict(orient='records')
    

sys.stdout.write(simplejson.dumps(records, ignore_nan=True))    
rejected.to_csv('./rejected.csv', index=False)
df.to_csv("./df_patient_transform.csv", index=False)







