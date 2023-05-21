import json
import datetime;

# Read the JSON file
file_path = './t.json'
with open(file_path) as file:
    # Load JSON data from the file
    x = json.load(file)

filtered_data = []
new_fichier_patient = []
current_time = datetime.datetime.now()
current_year = current_time.year

modified_time = current_time.replace(year=current_year - 125)  # Subtracting 1 from the current year

print(current_time.strftime("%Y-%m-%d %H:%M:%S"))
print(modified_time.strftime("%Y-%m-%d %H:%M:%S"))


"""
for data in x["FichierPatient"]:
    if data["DATEOFBIRTH"] is None or data["DATEOFBIRTH"]=="":
        filtered_data.append({
            "PATIENTNUMBER": data["PATIENTNUMBER"],
            "EXTRA_DATEOFDEATH": data["EXTRA_DATEOFDEATH"],
            "RULES": "NULL",
            "ACTION": "Avertissement",
            "MESSAGE": "La date de décès doit être renseignée"
        })
    else:
        new_fichier_patient.remove(data)
"""

        
