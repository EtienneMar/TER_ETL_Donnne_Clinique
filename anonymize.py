import pandas as pd
from faker import Faker

# Read excel file
excel_file = pd.ExcelFile('Anonymisation.xlsx')

# Get list of sheet names
sheet_names = excel_file.sheet_names

# Import Faker
faker = Faker()

# Create a dictionary to hold dataframes for each sheet
dict_df = {}
for sheet_name in sheet_names:
    dict_df[sheet_name] = excel_file.parse(sheet_name)

# Iterate through all sheets, find the PATIENT_IDENTIFICATION_NUMBER, and change names with same "PIN"
# and synchronise the change across all sheets

for sheet_name, df in dict_df.items():
    for pin in dict_df.values():
        id_to_modify = list(set(pin['PATIENT_IDENTIFICATION_NUMBER']))
        for i in range(len(id_to_modify)):
            new_name = faker.name()
            df.loc[df['PATIENT_IDENTIFICATION_NUMBER'] == id_to_modify[i], 'MEDICAL_RECORD_NAME'] = new_name
    dict_df[sheet_name] = df

# Save the anonymized Excel file
with pd.ExcelWriter('Anonymisation_anonym.xlsx') as writer:
    for sheet_name, df in dict_df.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)