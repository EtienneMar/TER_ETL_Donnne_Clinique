import pandas as pd
import requests
from datetime import datetime, timedelta
from hijri_converter import convert
import numpy as np
from pandas import *

def hijri_and_removeLeadingZero(data : pd.DataFrame, date=False,  removeLeadingZero=False):
    # Load the JSON data
    df = data.copy(); 
    
    # Convert hijri date to gregorian date
    def hijri_to_gregorian(date_str):
        if '-' in date_str:
            parts = date_str.split('-')
            if len(parts) == 3:
                if len(parts[0]) == 4:
                    return date_str  # La date est déjà grégorienne
                else:
                    try:
                        year, month, day = int(parts[2]), int(parts[1]), int(parts[0])
                        nowGregorian = datetime.now()
                        hijri_now = convert.Gregorian(nowGregorian.year, nowGregorian.month, nowGregorian.day).to_hijri()
                        url = "http://api.aladhan.com/v1/gToH/{}-{}-{}".format(nowGregorian.day, nowGregorian.month, nowGregorian.year-125)
                        response = requests.get(url)
                        hijri_limit = response.json()['data']
                        if response.status_code != 200:
                            print("Error while fetching data from the API")
                        if int(hijri_limit['hijri']['year']) <= year <= hijri_now.year and 1 <= month <= 12 and 1 <= day <= 30:  # Assurez-vous que la date est dans la plage prise en charge
                            hijri_date = convert.Hijri(year, month, day).to_gregorian()
                            return hijri_date.strftime('%Y-%m-%d %H:%M:%S')
                        else:
                            return None
                    except ValueError:
                        return None
        return date_str

 
    # Apply the conversion on the BIRTHDATE column if date=True
    
    rejected_columns = list(df.columns) + ['Message', 'Type']
    rejected = pd.DataFrame(columns=rejected_columns)


    if date:
        df['DateOfBirth'] = df['DateOfBirth'].apply(hijri_to_gregorian)
        today = datetime.now()
        date_limit = today - timedelta(days=125*365)
        for index, row in df.iterrows():
            date_value = (row['DateOfBirth'])
            if pd.to_datetime(date_value) > today :
                row['Type'] = 'rejected'
                row['Message'] = 'date supérieur à today' 
                row['Rule'] = 'V-DateOf-Birth-1'
                rejected = pd.concat([rejected,row.to_frame().T])
                continue
            elif pd.to_datetime(date_value) < date_limit :
                row['Type'] = 'rejected'
                row['Message'] = 'date supérieur à 125' 
                row['Rule'] = 'V-Today-1'
                rejected = pd.concat([rejected,row.to_frame().T])  
                continue    
            try:
                datetime.strptime(date_value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                row['Type'] = 'rejected'
                row['Message'] = 'Invalid date format. Must be YYYY-MM-DD HH: MM: SS'
                row['Rule'] = 'V-FormatDate-1' 
                rejected = pd.concat([rejected,row.to_frame().T])
        rejected = rejected[['PatientNumber', 'DateOfBirth', 'Type', 'Message']]
        
    if removeLeadingZero:
        for index, row in df.iterrows():
        # Vérification de chaque valeur dans la ligne
            for col in df.columns:
                val = str(row[col])
                if val.startswith('0') :
                    if len(val) == 1 :
                        df.loc[index, col] = np.nan
                    else : 
                        val = val.lstrip('0')
                        df.loc[index, col] = val
            
    #rejected.to_csv('../../', index=False)
    return [df, rejected]


def lenght_and_character_Columns(data: pd.DataFrame, columnName, numberLenghtLimit, lenghtColumns=False, alphaCharacter=False, typeRule_AlphaCharacter: str="reject"):
    
    """
    Returns a DataFrame containing the rows where the length of the specified column exceeds the given length limit.

    Args:
        data (pd.DataFrame): The input DataFrame.
        columnName (str): The name of the column to check.
        numberLengthLimit (int): The maximum length allowed for the column values.
        lengthColumns (bool, optional): If True, check the length of all columns. Defaults to False.
        alphaCharacter (bool, optional): If True, only check columns containing alphabetical characters. Defaults to False.
        type (str, optional): Whether to reject or flag rows that exceed the length limit. Can be "reject" or "advert". Defaults to "reject".

    Returns:
        pd.DataFrame: A DataFrame containing the rows where the specified column exceeds the length limit.
    """
    
    df = data.copy()
    df = df.reset_index().rename(columns={'index': 'Row_id'})
    
    if columnName not in df.columns:
        raise ValueError(f"Column '{columnName}' does not exist in the DataFrame")

    if df[columnName].isna().any():
        df[columnName].fillna('null', inplace=True)
    
    df_long_names = pd.DataFrame()
    df_alpha= pd.DataFrame()
    
    if lenghtColumns : 
        df_long_names = df[df[columnName].str.len() > numberLenghtLimit] 
        df_long_names = df_long_names[['Row_id','PatientNumber', columnName]]
        df_long_names['Type'] = 'warning'
        df_long_names['Message'] = 'La longueur ne doit pas dépasser '+str(numberLenghtLimit)+' Caractères'
        df_long_names['Rule'] = 'V-length'+str(numberLenghtLimit) 
    if alphaCharacter : 
        df_alpha = df[df[columnName].str.isalnum()]
        df_alpha = df_alpha[['Row_id','PatientNumber', columnName]]
        if typeRule_AlphaCharacter == "reject" : 
            df_alpha['Type'] = 'rejected'
            df_alpha['Rule'] = 'V-Alpha-1'
        elif typeRule_AlphaCharacter == "warn" :
            df_alpha['Type'] = 'warning'
            df_alpha['Rule'] = 'V-Alpha-2'
        df_alpha['Message'] = 'Alpha characters only'
        df_alpha['ColumnsName'] = columnName
        
        
        
    df_result = pd.concat([df_long_names, df_alpha])
    
    return df_result

def NotNull (df : pd.DataFrame, columnName, type: str="reject") : 
    
    # Vérifier si columnName est dans la liste des colonnes
    if columnName not in df.columns:
        raise ValueError(f"Column '{columnName}' does not exist in the DataFrame")
    
    # Sélectionner les lignes avec des valeurs nulles dans la colonne
    df_null_values = df[df[columnName].isnull()]
    df_null_values = df_null_values[['PatientNumber', columnName]]
    if type == "reject" : 
        df_null_values['Type'] = 'rejected'
        df_null_values['Rule'] = 'V-NotNull-1'
    elif type == "warn" :
        df_null_values['Type'] = 'warning'
        df_null_values['Rule'] = 'V-NotNull-2'
    df_null_values['Message'] = 'Valeur ne peut pas être null ou vide'
    
    return df_null_values