from operator import truediv
import sys
import pandas as pd
import datetime
from datetime import datetime, timedelta
import numpy as np
import json
from excel import create_excel
import math
import csv
"""def get_rules_from_nifi_properties(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('columns_and_rules='):
                json_str = line.strip().split('=')[1]
                return json.loads(json_str)
    return None"""

def V_today1(df, column_name, reject_list,rejections_count):
    today = datetime.now()
    rule_name = 'V-Today-1'
    def check_date(row):
        dob = pd.to_datetime(row[column_name], errors='coerce')
        if dob > today:
            row_copy = row.copy()
            row_copy['Rejet'] = rule_name
            reject_list.concat(row_copy)
            rejections_count[rule_name][column_name] += 1
            return False
        return True
    df = df[df.apply(check_date, axis=1)]
    return df


def V_date_of_birth1(df, column_name,reject_list,rejections_count):
    today = datetime.now()
    max_dob = today - timedelta(days=125 * 365)
    rule_name = 'V-DateOfBirth-1'
    def check_dates(row):
        dob = pd.to_datetime(row[column_name], errors='coerce')
        
        if dob is not pd.NaT and dob < max_dob:
            row_copy = row.copy()
            row_copy['Rejet'] = rule_name
            reject_list.append(row_copy)
            rejections_count[rule_name][column_name] += 1
            return False

        return True

    df = df[df.apply(check_dates, axis=1)]

    return df

def V_dateOfDeath(df, column_name,reject_list,rejections_count):
    rule_name = 'V-DateofDeath'
    def check_dates(row):
        if 'DATAOFBIRTH' in df.columns :
            dob = pd.to_datetime(row['DATEOFBIRTH'], errors='coerce')
            dod = pd.to_datetime(row[column_name], errors='coerce')
            
            if dod is not pd.NaT and dob is not pd.NaT and dod < dob:
                row_copy = row.copy()
                row_copy['Rejet'] = rule_name
                reject_list.append(row_copy)
                rejections_count[rule_name][column_name] += 1
                return False

            return True
        else :
            return True
    df = df[df.apply(check_dates, axis=1)]

    return df

def D_patientDeceased(row,column_name):
    if pd.isna(row['PATIENTDECEASED']):
        if pd.notna(row[column_name]):
            return 'Oui'
    return row['PATIENTDECEASED']


def T_RemoveLeadingZero_1(row, column_name):
    value = row[column_name]
    if isinstance(value, str) and value.startswith('0'):
        row[column_name] = value.lstrip('0')
    return row[column_name]

def V_NotNull1(row,column_name, reject_list,rejections_count):
    rule_name = 'V-NotNull-1'
    if pd.isna(row[column_name]) or row[column_name] == '':
        row_copy = row.copy()
        row_copy['Rejet'] = rule_name
        reject_list.append(row_copy)
        rejections_count[rule_name][column_name] += 1
        return False
    return True

def V_NotNull2(row,column_name, warnings_list, warnings_count):
    rule_name = 'V-NotNull-2'
    if pd.isna(row[column_name]) or row[column_name] == '':
        row_copy = row.copy()
        row_copy['Avertissement'] = rule_name
        warnings_list.append(row_copy)
        warnings_count[rule_name][column_name] += 1

def V_length50(row, column_name, warnings_list, warnings_count):
    rule_name = 'V-length50'
    if len(str(row[column_name])) > 50:
        row_copy = row.copy()
        row_copy['Avertissement'] = rule_name
        warnings_list.append(row_copy)
        warnings_count[rule_name][column_name] += 1

def V_length100(row, column_name, warnings_list, warnings_count):
    rule_name = 'V-length100'
    if len(str(row[column_name])) > 100:
        row_copy = row.copy()
        row_copy['Avertissement'] = rule_name
        warnings_list.append(row_copy)
        warnings_count[rule_name][column_name] += 1

def V_alpha1(row, column_name,reject_list, rejections_count):
    rule_name = 'V-alpha-1'
    if not str(row[column_name]).isalpha():
        row_copy = row.copy()
        row_copy['Rejet'] = rule_name
        reject_list.append(row_copy)
        rejections_count[rule_name][column_name] += 1
        return False
    return True

def V_alpha2(row, column_name,warnings_list, warnings_count):
    rule_name = 'V-alpha-2'
    if not str(row[column_name]).isalpha():
        row_copy = row.copy()
        row_copy['Avertissement'] = rule_name
        warnings_list.append(row_copy)
        warnings_count[rule_name][column_name] += 1


def T_EncounterNumber_1(df, file_type, row,column_name):
    if file_type in ['Transfer','Diagnosis','Procedure']:
        if 'HOSPITAL' in df.columns :
            return f"{row['HOSPITAL']}-IP-{row[column_name]}"
        else :
            return f"NULL-IP-{row[column_name]}"
    elif file_type == 'Service':
        encounter_type = "IP" if 'ENCOUNTERTYPE' not in df.columns or pd.isnull(row['ENCOUNTERTYPE']) else row['ENCOUNTERTYPE']
        if 'HOSPITAL' in df.columns :
            return f"{row['HOSPITAL']}-{encounter_type}-{row[column_name]}"
        else :
            return f"NULL-{encounter_type}-{row[column_name]}"
    else :
        if 'HOSPITAL' in df.columns :
            return f"{row['HOSPITAL']}-{row['ENCOUNTERTYPE']}-{row[column_name]}"
        else :
            return f"NULL-{row['ENCOUNTERTYPE']}-{row[column_name]}"

def T_PatientNumber_1(df, row,column_name):
    if 'HOSPITAL' in df.columns :
        return f"{row['HOSPITAL']}-{row[column_name]}"
    else :
        return f"NULL-{row[column_name]}"

def T_BedNumber_1(df, row, column_name):
    if 'ROOMNUMBER' in df.columns :
        if 'HOSPITAL' in df.columns :
            return f"{row['HOSPITAL']}-{row['WARD']}-{row['ROOMNUMBER']}-{row[column_name]}"
        else :
            return f"NULL-{row['WARD']}-{row['ROOMNUMBER']}-{row[column_name]}"
    else :
        if 'HOSPITAL' in df.columns :
            return f"{row['HOSPITAL']}-{row['WARD']}-NULL-{row[column_name]}"
        else :
            return f"NULL-{row['WARD']}-NULL-{row[column_name]}"

def T_RoomNumber_1(df,row, room_number_column):
    if 'HOSPITAL' in df.columns :
        room_number_combined = f"{row['HOSPITAL']}-{row['WARD']}-{row[room_number_column]}"
    else :
        room_number_combined = f"NULL-{row['WARD']}-{row[room_number_column]}"

    row[room_number_column] = room_number_combined
    return row


def D_BedNumber_1(df, row, warnings_list, warnings_count):
    
    rule_name = 'D-BedNumber-1'
    bed_number = row['BEDNUMBER'] #if pd.notnull(row['BEDNUMBER']) else 'NULL'
    
    if row['BEDNUMBER'] == 'NULL' :
        row_copy = row.copy()
        row_copy['Avertissement'] = rule_name
        warnings_list.append(row_copy)
        warnings_count[rule_name]['BEDNUMBER'] += 1
    if 'ROOMNUMBER' in df.columns :
        if 'HOSPITAL' in df.columns :
            return f"{row['HOSPITAL']}-{row['WARD']}-{row['ROOMNUMBER']}-{bed_number}"
        else :
            return f"NULL-{row['WARD']}-{row['ROOMNUMBER']}-{bed_number}"
    else :
        if 'HOSPITAL' in df.columns :
            return f"{row['HOSPITAL']}-{row['WARD']}-NULL-{bed_number}"
        else :
            return f"NULL-{row['WARD']}-NULL-{bed_number}"
        
def D_RoomNumber_1(df, row, warnings_list, warnings_count):
    rule_name = 'D-RoomNumber-1'
    room_number = row['ROOMNUMBER'] #if pd.notnull(row['ROOMNUMBER']) else 'NULL'  
    if row['ROOMNUMBER'] == 'NULL':
        row_copy = row.copy()
        row_copy['Avertissement'] = rule_name
        warnings_list.append(row_copy)
        warnings_count[rule_name]['ROOMNUMBER'] += 1
    if 'HOSPITAL' in df.columns :
        return f"{row['HOSPITAL']}-{row['WARD']}-{room_number}"
    else :
        return f"NULL-{row['WARD']}-{room_number}"


def D_Sequence_1(df, patient_col, date_col):
    # Trier le DataFrame par date de diagnostic pour chaque patient
    df = df.sort_values(by=[patient_col, date_col])
    
    # Créer une nouvelle colonne qui numérote chaque ligne pour chaque patient
    df['SEQUENCE'] = df.groupby(patient_col).cumcount() + 1

    # Récupérer la liste des colonnes
    cols = df.columns.tolist()

    # Placer la colonne 'SEQUENCE' avant 'EXTRA:DIAGNOSISTYPE'
    cols.insert(cols.index('EXTRA:DIAGNOSISTYPE'), cols.pop(cols.index('SEQUENCE')))
    
    # Réorganiser les colonnes du DataFrame
    df = df[cols]
    
    return df

def T_RoundNum92_1(row, column_name):
    # Vérifiez si la valeur peut être convertie en float
    try:
        float_value = float(row[column_name])
        return round(float_value, 2)
    except ValueError:
        # Si la valeur ne peut pas être convertie en float, retournez la valeur originale
        return row[column_name]

def V_Num_1(row, column_name, reject_list, rejections_count):
    rule_name = 'V-Num-1'
    if not str(row[column_name]).isnumeric():
        row_copy = row.copy()
        row_copy['Rejet'] = rule_name
        reject_list.append(row_copy)
        rejections_count[rule_name][column_name] += 1
        return False
    return True

def V_Quantity_1(row, column_name, reject_list, rejections_count):
    rule_name = 'V-Quantity-1'
    value = pd.to_numeric(row[column_name], errors='coerce')
    if pd.isnull(value) or value <= 0:
        row_copy = row.copy()
        row_copy['Rejet'] = rule_name
        reject_list.append(row_copy)
        rejections_count[rule_name][column_name] += 1
        return False
    return True


def D_DummyEncounterNumber_1(row):
    encounter_number = f"{row['HOSPITAL']}-{row['PATIENTNUMBER']}-{row['SERVICINGDEPARTMENT']}-{row['STARTDATETIME'].strftime('%d%m%Y')}"
    return encounter_number

def V_GTE0_1(row, column_name, reject_list, rejections_count):
    rule_name = 'V-GTE0-1'
    if pd.isna(row[column_name]) or not int(row[column_name]) >= 0:
        row_copy = row.copy()
        row_copy['Rejet'] = rule_name
        reject_list.append(row_copy)
        rejections_count[rule_name][column_name] += 1
        return False
    return True

################################################ 
#On est censés avoir Age? ou on le construit nous même par cette méthode??
def D_Age_1(row,column_name_age, warnings_list, warnings_count):
    rule_name = 'D-Age-1'
    
    if pd.notnull(row['DATEOFBIRTH']):
        age_years = row['STARTDATETIME'].year - row['DATEOFBIRTH'].year
        if row['STARTDATETIME'].month < row['DATEOFBIRTH'].month or (row['STARTDATETIME'].month == row['DATEOFBIRTH'].month and row['STARTDATETIME'].day < row['DATEOFBIRTH'].day):
            age_years -= 1
        
        if age_years != row[column_name_age]:
            row_copy = row.copy()
            row_copy['Avertissement'] = rule_name
            warnings_list.append(row_copy)
            warnings_count[rule_name][column_name_age] += 1
        
        return age_years
    else:
        return row[column_name_age]  # Conserve la valeur originale si DateOfBirth est NULL

#CELLE LA S'APPLIQUE SUR QUOI??
def D_Null_1(row, column_name):
    value = row[column_name]
    if value == '':
        row[column_name] = 'NULL'
    return row[column_name]


#TROP BIZARRE CETTE REGLE FAUT DEMANDER A MR BILEL
def D_Duration_1(row, column_name_duration, warnings_list, warnings_count):
    rule_name = 'D-Duration-1'
    if pd.notnull(row['ENDDATETIME']):
        end_datetime = pd.to_datetime(row['ENDDATETIME'])
        start_datetime = pd.to_datetime(row['STARTDATETIME'])
        duration = (end_datetime - start_datetime).total_seconds() / 60.0
        duration = round(duration)  # convert to integer
        if duration != int(row[column_name_duration]):
            row_copy = row.copy()
            row_copy['Avertissement'] = rule_name
            warnings_list.append(row_copy)
            warnings_count[rule_name][column_name_duration] += 1
        return duration
    else:
        return row[column_name_duration]  # keep the original value if 'EndDateTime' is NULL

def T_RoundInteger_1(row, column_name):
    value = row[column_name]
    return math.ceil(value)

#################################################################################
def enlever_all_null_colonnes(df):
    for col in df.columns:
        if df[col].isna().all():
            df.drop(col, axis=1, inplace=True)


def deduplicate(input_csv, rejections_count, file_type):
    rule_name = 'Deduplication'
    deduplicated_df = None
    duplicates_df = None

    if file_type == 'Patient':
        deduplicated_df = input_csv.drop_duplicates(subset='PATIENTNUMBER', keep='first')
        duplicates_df = input_csv[input_csv.duplicated(subset='PATIENTNUMBER', keep='first')]
        duplicates_df = duplicates_df.assign(Rejet='Duplication')
    else:
        deduplicated_df = input_csv.drop_duplicates(keep='first')
        duplicates_df = input_csv[input_csv.duplicated(keep='first')]
        duplicates_df = duplicates_df.assign(Rejet='Duplication')

    nb_lignes_dupliquees = len(input_csv) - len(deduplicated_df)
    rejections_count[rule_name]['/'] = nb_lignes_dupliquees

    return deduplicated_df, duplicates_df

def recuperate(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def main():
    #TODO list :
    file_type_path = "./file_type.txt"
    # Récupération du nom du fichier d'entrée
    file_type = recuperate(file_type_path)
    
    file_name_path = "./file_name.txt"
    # Récupération du nom du fichier d'entrée
    file_name = recuperate(file_name_path)    
    
    rules={
            "DATEOFBIRTH": ["V_today1", "V_dateOfBirth1","V_NotNull2"], 
            "DATEOFDEATH": ["V_today1", "V_dateOfBirth1","V_dateOfDeath", "D_patientDeceased","V_NotNull2"],
            "EXTRA:DATEOFDEATH": ["V_today1", "V_dateOfBirth1","V_dateOfDeath", "D_patientDeceased","V_NotNull2"],
            "STARTDATETIME": ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull1"],
            "ENDDATETIME": ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull1"],
            "PROCEDUREDATETIME":["V_today1", "V_dateOfBirth1","V_dateOfDeath","D_Sequence_1","V_NotNull2"],
            "EXTRA:PRETRIAGETIME":["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:TRIAGESTARTTIME":["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:TRIAGEENDTIME":["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:CANCELLATIONDATE":["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:DIAGNOSISDATETIME":["V_today1", "V_dateOfBirth1","V_dateOfDeath","D_Sequence_1","V_NotNull2"],
            "ORDERDATETIME" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:STARTDATETREATMENTPLAN" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:ENDDATETREATMENTPLAN" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:RADIOLOGISTREPORTDATETIME" :["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:RADIOLOGISTFINALISATIONDATE" :["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:COLLECTIONTIME" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:SAMPLERECEIVEDTIME" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:SIGNATUREDATETIME" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:STARTDISPENSETIME" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:PRESCRIPTIONVALIDATIONTIME" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:PREOPSTART": ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:PREOPEND" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:ANAETHESIASTART" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:ANAETHESIAEND" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:RECOVERYSTART" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:RECOVERYEND" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "EXTRA:PLANNEDSURGERYDATE" : ["V_today1", "V_dateOfBirth1","V_dateOfDeath","V_NotNull2"],
            "HOSPITAL": ["V_NotNull1"],
            "PATIENTNUMBER" : ["V_length50", "T_PatientNumber_1"],
            "FATHERSNAME": ["V_length100", "V_alpha2"], 
            "FATHERSPRENAME": ["V_length100", "V_alpha2"],
            "PLACEOFBIRTH": ["V_length100"],
            "PATIENTDECEASED" : ["D_patientDeceased"],
            "TITLE" :  ["V_alpha2", "V_dateOfBirth1","V_today1"],
            "ENCOUNTERNUMBER" :  ["V_NotNull1", "T_EncounterNumber_1"],
            "BEDNUMBER" :  ["T_BedNumber_1", "D_BedNumber_1"],
            "AGE" :  ["D_Age_1"],
            "ROOMNUMBER" : ["T_RoomNumber_1", "D_RoomNumber_1"],
            "DIAGNOSISCODE" : ["V_NotNull1"],
            "DIAGNOSISVERSION" : ["V_NotNull1"],
            "SEQUENCE" : ["V_NotNull1","V_Num_1", "T_RoundInteger_1"],
            "PROCEDUREVERSION" :  ["V_NotNull1"],
            "QUANTITY" : ["V_NotNull1", "V_Quantity_1" , "T_RoundNum92_1"],
            "DURATION" : ["V_GTE0_1","D_Duration_1",  "T_RoundNum92_1"],
            "SERVICEDESCRIPTION" : ["V_length100"],
            }

    df = pd.read_csv(sys.stdin, dtype=str)
    initial_row_count = len(df)
    
    #TODO : ajouter toutes les règles ici
    warnings_count = {
        "V-length50": {},
        "V-length100": {},
        "V-alpha-2": {},
        "V-NotNull-2": {},
        "D-BedNumber-1": {},
        "D-RoomNumber-1": {},
        "D-Age-1": {},
        "D-Duration-1": {},
        "D_BedNumber_1":{},
        "D_RoomNumber_1":{}
    }

    rejections_count = {
        "V-NotNull-1": {},
        "V-alpha-1": {},
        "V-Today-1": {},
        "V-DateOfBirth-1": {},
        "V-DateofDeath": {},
        "Deduplication": {},
        "V-Quantity-1": {},
        "V-GTE0-1": {},
        "V-Num-1": {}
    }

    # Initialisation des dictionnaires de dictionnaires
    for rule_dict in (warnings_count, rejections_count):
        for rule_name in rule_dict:
            rule_dict[rule_name] = {column_name: 0 for column_name in rules.keys()}

    df, duplicates_df = deduplicate(df,rejections_count,file_type)
    
    warnings_list = []
    reject_list = []

    validation_functions = {
        "V_today1": V_today1,
        "V_dateOfBirth1": V_date_of_birth1,
        "V_dateOfDeath": V_dateOfDeath,
        "D_patientDeceased": D_patientDeceased,
        "V_NotNull1": V_NotNull1,
        "V_NotNull2": V_NotNull2,
        "V_length50": V_length50,
        "V_length100": V_length100,
        "V_alpha1": V_alpha1,
        "V_alpha2": V_alpha2,
        "T_RemoveLeadingZero_1": T_RemoveLeadingZero_1,
        "D_Null_1": D_Null_1,
        "T_BedNumber_1": T_BedNumber_1,
        "T_PatientNumber_1": T_PatientNumber_1,
        "T_EncounterNumber_1" : T_EncounterNumber_1,
        "D_BedNumber_1" : D_BedNumber_1,
        "T_RoomNumber_1" : T_RoomNumber_1,
        "V_Num_1" : V_Num_1,
        "D_Age_1" : D_Age_1,
        "D_Null_1" : D_Null_1,
        "T_RoundNum92_1" : T_RoundNum92_1,
        "V_GTE0_1" : V_GTE0_1,
        "D_Duration_1" : D_Duration_1,
        "D_RoomNumber_1" : D_RoomNumber_1,
        "V_Quantity_1" : V_Quantity_1,
        "T_RoundInteger_1" : T_RoundInteger_1,
        "D_DummyEncounterNumber_1" : D_DummyEncounterNumber_1,
        "D_Sequence_1" : D_Sequence_1
    }
    
    if 'BEDNUMBER' not in df.columns and file_type == 'Transfer':
        df['BEDNUMBER'] = 'NULL'
    elif 'ROOMNUMBER' not in df.columns and file_type == 'Transfer':
        df['ROOMNUMBER'] = 'NULL'
    
    for column, functions in rules.items():
        if column not in df.columns:
            continue  # Skip to the next column if it doesn't exist in the DataFrame
        
        for function_name in functions:
            if function_name in validation_functions:
                function = validation_functions[function_name]
                
                if function_name == "D_patientDeceased":
                    df['PATIENTDECEASED'] = df.apply(lambda row: function(row, column), axis=1)
                
                elif function_name in ["T_RemoveLeadingZero_1","D_Null_1","T_RoundNum92_1","T_RoundInteger_1","D_DummyEncounterNumber_1"]:  # Ajoutez ici le nom de votre règle
                    df[column] = df.apply(lambda row: function(row, column), axis=1)
                
                elif function_name == "T_EncounterNumber_1":
                    df[column] = df.apply(lambda row: function(df, file_type, row, column), axis=1)
            
                elif function_name == "T_PatientNumber_1":
                    df[column] = df.apply(lambda row: function(df, row, column), axis=1)
                
                elif function_name in ["T_BedNumber_1", "T_RoomNumber_1"]:
                    df.apply(lambda row: function(df, row, column), axis=1)
                
                elif function_name in ["D_BedNumber_1","D_RoomNumber_1"]:
                    df[column] = df.apply(lambda row: function(df, row, warnings_list,warnings_count), axis=1)
                
                elif function_name in ["V_length50", "V_length100", "V_alpha2","V_NotNull2","D_Age_1","D_Duration_1"]:
                    df.apply(lambda row: function(row, column, warnings_list, warnings_count), axis=1)
                
                elif function_name in ["V_NotNull1","V_alpha1","V_GTE0_1","V_Quantity_1","V_Num_1"] :
                    df = df[df.apply(lambda row: function(row, column,reject_list, rejections_count), axis=1)]
                
                elif function_name == "D_Sequence_1" :
                    df = function(df, 'PATIENTNUMBER',column)
                
                else:
                    df = function(df, column,reject_list, rejections_count)

    if file_type == 'Service':
        df['STARTDATETIME'] = pd.to_datetime(df['STARTDATETIME'])
        df['DUMMYENCOUNTERNUMBER'] = df.apply(D_DummyEncounterNumber_1, axis=1)
        df = df.drop('ENCOUNTERTYPE', axis=1) if 'ENCOUNTERTYPE' in df.columns else df
    
    if file_type =='Patient':
        df = df.drop('HOSPITAL', axis=1)        
    
    #FileDateCreation
    df = df.reset_index(drop=True)
    file_date_creation = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df.loc[0, 'LASTUPDATEDATETIME'] = file_date_creation
    
    # Ajouter les lignes avec des avertissements et des rejets au dataframe lines_df pour pouvoir les écrire dans le validation report après
    lines_df = pd.DataFrame()
    warnings_df = pd.DataFrame(warnings_list)
    rejections_df = pd.DataFrame(reject_list)
    lines_df = pd.concat([lines_df, duplicates_df, warnings_df, rejections_df], ignore_index=True)


    create_excel(lines_df,initial_row_count,warnings_count,rejections_count, file_name, file_type)


    # Supprimer les colonnes qui contiennent uniquement des valeurs NULL pour toutes les lignes
    enlever_all_null_colonnes(df)

    df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
