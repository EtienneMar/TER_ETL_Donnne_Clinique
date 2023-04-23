import pandas as pd

# Read excel file with sheet name
dict_df = pd.read_excel('Anonymisation.xlsx', sheet_name=['Radiology','Pharmacy', 'Coding_Diagnosis'])

# # Import Faker
from faker import Faker
faker = Faker()
#Test fake data generation
#print("The Faker library can generate fake names. By running 'faker.name()', we get:")
#print(faker.name())


# for sheet_name, pin in dict_df.items():
#     print(list(set(pin['PATIENT_IDENTIFICATION_NUMBER'])))


for sheet_name, df in dict_df.items():
    for sheet_name, pin in dict_df.items():
        id_to_modify = list(set(pin['PATIENT_IDENTIFICATION_NUMBER']))
        for i in range (len(id_to_modify)):
            new_name = faker.name()
            df.loc[df['PATIENT_IDENTIFICATION_NUMBER'] == id_to_modify[i], 'MEDICAL_RECORD_NAME'] = new_name
            dict_df[sheet_name] = df

# Save updated Excel file
with pd.ExcelWriter('Anonymisation_updated.xlsx') as writer:
    for sheet_name, df in dict_df.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)