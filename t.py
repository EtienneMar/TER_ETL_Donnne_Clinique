# List of database fields
db_fields = [
    "SourcePatientNumber",
    "Hospital",
    "BedNumber",
    "EncounterNumber",
    "Ward",
    "StartDateTime",
    "RoomNumber",
    "WardType",
    "Leave",
    "LeaveType",
    "AttendingConsultant_Code",
    "AttendingConsultantName",
    "AttendingConsultant_SpecialtyCode",
    "LastUpdateDateTime",
    "Site"
]

# List of mapping fields
map_fields = [
    "PatientNumber",
    "Extra:Hospital",
    "BedNumber",
    "EncounterNumber",
    "Ward",
    "StartDateTime",
    "Extra:RoomNumber",
    "Extra:WardType",
    "Leave",
    "Extra:LeaveType",
    "AttendingConsultant_Code",
    "Extra:AttendingConsultantName",
    "AttendingConsultant_SpecialtyCode",
    "Extra:LastUpdateDateTime",
    "Extra:Site"
]

# Create the mapping table as a dictionary
mapping_table = dict(zip(db_fields, map_fields))


def map_headers(header_row, mapping_table):
    # Initialize the list for mapped and unmapped headers
    mapped_headers = {}
    unmapped_headers = []

    for header in header_row:
        # Try to get the mapped field
        mapped_field = mapping_table.get(header)

        if mapped_field:
            # If a mapped field is found, add it to the mapped headers list
            mapped_headers[header] = mapping_table.pop(header)
        else:
            # If no mapped field is found, add the header to the unmapped headers list
            unmapped_headers.append(header)

    # Return the mapped headers and the unmapped headers
    return mapped_headers, unmapped_headers

# Test the function with a sample header row
header_row = ['SourcePatientNumber', 'Hospital', 'UnknownField']
mapped_headers, unmapped_headers = map_headers(header_row, mapping_table)

print(f'Mapped headers: {mapped_headers}')
print(f'Unmapped headers: {unmapped_headers}')
print(mapping_table.values())





     #Gestion des Headers en fonction du types des fichiers
        if "HOSPITAL" not in header_row :
            #secure_filename returns a safe version of the filename, 
            # ensuring there are no relative paths or invalid characters.
            filename = secure_filename(file.filename)
            if extract_hospital(filename) is not None : 
                header_row.append("HOSPITAL")
            
        if "ENOUNTERTYPE" not in header_row and type_fichier =='Encounter': 
            filename = secure_filename(file.filename)
            if extract_hospital(filename) is not None : 
                header_row.append("ENC")
        if 
        
        #Réponse JSON test des colonnes obligatoires (mandatoryField)
        cursor.execute("SELECT mandatoryField FROM fichier_table WHERE typeFichier = %s", (type_fichier,))
        mandatory_fields = cursor.fetchone()[0]
        mandatory_fields = json.loads(mandatory_fields)
        missing_fields = []
        for mandatory_field in mandatory_fields:
            if mandatory_field not in header_row:
                missing_fields.append(mandatory_field)
        if missing_fields:
            return jsonify({'error': 'Champs obligatoires manquants', 'missing_fields': missing_fields, 'header' : header_row}), 400
    