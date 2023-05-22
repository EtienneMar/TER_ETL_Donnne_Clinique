CREATE TABLE FieldMapping (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    FileInputField VARCHAR(255),
    FieldOutputField VARCHAR(255)
);

INSERT INTO FieldMapping (FileInputField, FieldOutputField)
VALUES
    ('MRN Number', 'PATIENTNUMBER'),
    ('Hospital', 'EXTRA_HOSPITAL'),
    ('DateOfBirth', 'DATEOFBIRTH'),
    ('Gender', 'GENDER'),
    ('PatientDeceased', 'EXTRA_PATIENTDECEASED'),
    ('DateofDeath', 'EXTRA_DATEOFDEATH'),
    ('PlaceOfBirth', 'EXTRA_PLACEOFBIRTH'),
    ('EthnicOrigin', 'ETHNICORIGIN'),
    ('Nationality', 'EXTRA_NATIONALITY'),
    ('LastName', 'LASTNAME'),
    ('FirstName', 'FIRSTNAME'),
    ('Title', 'TITLE'),
    ('MothersName', 'EXTRA_MOTHERSLASTNAME'),
    ('MothersPreName', 'EXTRA_MOTHERSFIRSTNAME'),
    ('FathersName', 'EXTRA_FATHERSLASTNAME'),
    ('FathersPreName', 'EXTRA_FATHERSFIRSTNAME'),
    ('FamilyDoctor', 'EXTRA_FAMILYDOCTOR'),
    ('BloodRefusal', 'EXTRA_BLOODREFUSAL'),
    ('OrganDonor', 'EXTRA_ORGANDONOR'),
    ('PrefLanguage', 'EXTRA_PREFLANGUAGE'),
    ('LastUpdateDateTime', 'EXTRA_LASTUPDATEDATETIME'),
    ('NationalID', 'NATIONALIDENTIFIER'),
    ('SourcePatientNumber', 'PATIENTNUMBER'),
    ('StartDateTime', 'STARTDATETIME'),
    ('EndDateTime', 'ENDDATETIME'),
    ('EncounterNumber', 'ENCOUNTERNUMBER'),
    ('Age', 'AGE'),
    ('EnounterType', 'ENOUNTERTYPE'),
    ('EncounterCategory', 'ENCOUNTERCATEGORY'),
    ('LengthOfStay', 'LENGTHOFSTAY'),
    ('AdmitWard', 'ADMITWARD'),
    ('DischargeWard', 'DISCHARGEWARD'),
    ('ReferringConsultant', 'REFERRINGCONSULTANT'),
    ('ReferringConsultantName', 'EXTRA_REFERRINGCONSULTANTNAME'),
    ('ReferringConsultantSpecialty', 'REFERRINGCONSULTANTSPECIALTY'),
    ('AdmittingConsultant', 'ADMITTINGCONSULTANT'),
    ('AdmittingConsultantName', 'EXTRA_ADMITTINGCONSULTANTNAME'),
    ('AdmittingConsultantSpecialty', 'ADMITTINGCONSULTANTSPECIALTY'),
    ('AttendingConsultant', 'ATTENDINGCONSULTANT'),
    ('AttendingConsultantName', 'EXTRA_ATTENDINGCONSULTANTNAME'),
    ('AttendingConsultantSpecialty', 'ATTENDINGCONSULTANTSPECIALTY'),
    ('DischargeConsultant', 'DISCHARGECONSULTANT'),
    ('DischargeConsultantName', 'EXTRA_DISCHARGECONSULTANTNAME'),
    ('DischargeConsultantSpecialty', 'DISCHARGECONSULTANTSPECIALTY'),
    ('TransferToHospital', 'EXTRA_TRANSFERTOHOSPITAL'),
    ('CauseOfDeath', 'EXTRA_CAUSEOFDEATH'),
    ('TypeOfDeath', 'EXTRA_TYPEOFDEATH'),
    ('Autopsy', 'EXTRA_AUTOPSY'),
    ('DRG1', 'DRG1'),
    ('DRG1Version', 'DRG1VERSION'),
    ('DRGGravity', 'EXTRA_DRGGRAVITY'),
    ('MDC', 'EXTRA_MDC'),
    ('DischargeDestination', 'DISCHARGEDESTINATION'),
    ('Address', 'ADDRESS'),
    ('PostCode', 'POSTCODE'),
    ('Municipality', 'EXTRA_MUNICIPALITY'),
    ('Suburb', 'SUBURB'),
    ('Region', 'EXTRA_REGION'),
    ('Country', 'EXTRA_COUNTRY'),
    ('LivingArrangements', 'EXTRA_LIVINGARRANGEMENTS'),
    ('MaritalStatus', 'MARITALSTATUS'),
    ('AdmissionCategory', 'ADMISSIONCATEGORY'),
    ('AdmissionSource', 'ADMISSIONSOURCE'),
    ('AdmissionElection', 'ADMISSIONELECTION'),
    ('HealthFund', 'HEALTHFUND'),
    ('FinancialClass', 'FINANCIALCLASS'),
    ('TransferFromHospital', 'EXTRA_TRANSFERFROMHOSPITAL'),
    ('ClinicName', 'EXTRA_CLINICNAME'),
    ('ClinicSpecialtyCode', 'EXTRA_CLINICSPECIALTYCODE'),
    ('ClinicSpecialty', 'EXTRA_CLINICSPECIALTY'),
    ('ModeOfArrival', 'EXTRA_MODEOFARRIVAL'),
    ('PreTriageTime', 'EXTRA_PRETRIAGETIME'),
    ('TriageStartTime', 'EXTRA_TRIAGESTARTTIME'),
    ('TriageEndTime', 'EXTRA_TRIAGEENDTIME'),
    ('DiagnosisOnDischarge', 'EXTRA_DIAGNOSISONDISCHARGE'),
    ('PhysicianSpecialityKey', 'EXTRA_PHYSICIANSPECIALITYKEY'),
    ('CancellationDate', 'EXTRA_CANCELLATIONDATE'),
    ('CancellationFlag', 'EXTRA_CANCELLATIONFLAG'),
    ('VisitType', 'EXTRA_VISITTYPE'),
    ('Site', 'EXTRA_SITE'),
    ('DischargeStatus', 'EXTRA_DISCHARGESTATUS'),
    ('ComplaintDesc', 'EXTRA_COMPLAINTDESC'),
    ('TriageCode', 'EXTRA_TRIAGECODE'),
    ('TriageDesc', 'EXTRA_TRIAGEDESC'),
    ('BedNumber', 'BEDNUMBER'),
    ('Ward', 'WARD'),
    ('RoomNumber', 'EXTRA_ROOMNUMBER'),
    ('WardType', 'EXTRA_WARDTYPE'),
    ('Leave', 'LEAVE'),
    ('LeaveType', 'EXTRA_LEAVETYPE'),
    ('AttendingConsultant_Code', 'ATTENDINGCONSULTANT_CODE'),
    ('AttendingConsultant_SpecialtyCode', 'ATTENDINGCONSULTANT_SPECIALTYCODE'),
    ('SourcePatientNumber', 'EXTRA_SOURCEPATIENTNUMBER'),
    ('DiagnosisCode', 'DIAGNOSISCODE'),
    ('DiagnosisVersion', 'DIAGNOSISVERSION'),
    ('Sequence', 'SEQUENCE'),
    ('DiagnosisType', 'EXTRA_DIAGNOSISTYPE'),
    ('ConditionOnset', 'CONDITIONONSET'),
    ('SequenceService', 'EXTRA_SEQUENCESERVICE'),
    ('PrimaryTumour', 'EXTRA_PRIMARYTUMOUR'),
    ('TumourCode', 'EXTRA_TUMOURCODE'),
    ('Metastase', 'EXTRA_METASTASE'),
    ('Ganglion', 'EXTRA_GANGLION'),
    ('StageEvolution', 'EXTRA_STAGEEVOLUTION'),
    ('Morphology', 'EXTRA_MORPHOLOGY'),
    ('Screening', 'EXTRA_SCREENING'),
    ('DiagnosisDateTime', 'EXTRA_DIAGNOSISDATETIME'),
    ('CodeCharacteristic', 'EXTRA_CODECHARACTERISTIC'),
    ('CodeCharacteristicDesc', 'EXTRA_CODECHARACTERISTICDESC'),
    ('LocalDiagCode', 'EXTRA_LOCALDIAGCODE'),
    ('LocalDiagCodeDesc', 'EXTRA_DIAGNOSISDESCRIPTION'),
    ('ProcedureDateTime', 'PROCEDUREDATETIME'),
    ('ProcedureCode', 'PROCEDURECODE'),
    ('ProcedureVersion', 'PROCEDUREVERSION'),
    ('InterventionType', 'EXTRA_INTERVENTIONTYPE'),
    ('Consultant', 'CONSULTANT'),
    ('ConsultantName', 'EXTRA_CONSULTANTNAME'),
    ('ConsultantSpecialty', 'CONSULTANTSPECIALTY'),
    ('ProcedureTheatre', 'PROCEDURETHEATRE'),
    ('LocalProcTheatre', 'EXTRA_LOCALPROCTHEATRE'),
    ('LocalProcTheatreDesc', 'EXTRA_LOCALPROCTHEATREDESC'),
    ('NbrProcedures', 'EXTRA_NBRPROCEDURES'),
    ('Hospital', 'HOSPITAL'),
    ('Quantity', 'QUANTITY'),
    ('ServiceCode', 'SERVICECODE'),
    ('PrimaryProcedure', 'EXTRA_PRIMARYPROCEDURE'),
    ('ServicingDepartment', 'SERVICINGDEPARTMENT'),
    ('Duration', 'DURATION'),
    ('ActualCharge', 'ACTUALCHARGE'),
    ('PointOfService1', 'POINTOFSERVICE1'),
    ('ServiceDescription', 'EXTRA_SERVICEDESCRIPTION'),
    ('ServiceGroup', 'EXTRA_SERVICEGROUP'),
    ('Clinic', 'CLINIC'),
    ('OrderDateTime', 'ORDERDATETIME'),
    ('PriorityCode', 'EXTRA_PRIORITYCODE'),
    ('Priority', 'EXTRA_PRIORITY'),
    ('StatusCode', 'EXTRA_STATUSCODE'),
    ('StartDateTreatmentPlan', 'EXTRA_STARTDATETREATMENTPLAN'),
    ('EndDateTreatmentPlan', 'EXTRA_ENDDATETREATMENTPLAN'),
    ('RequestNo', 'EXTRA_REQUESTNO'),
    ('OrderingDepartment', 'EXTRA_ORDERINGDEPARTMENT'),
    ('PrivateInsurance', 'EXTRA_PRIVATEINSURANCE'),
    ('OriginalServiceCode', 'EXTRA_ORIGINALSERVICECODE'),
    ('OriginalServiceDesc', 'EXTRA_ORIGINALSERVICEDESC'),
    ('OriginalServiceGroup', 'EXTRA_ORIGINALSERVICEGROUP'),
    ('RadiographerExamDuration', 'EXTRA_RADIOGRAPHEREXAMDURATION'),
    ('RadiologistLicence', 'EXTRA_RADIOLOGISTLICENCE'),
    ('RadiologistName', 'EXTRA_RADIOLOGISTNAME'),
    ('RadiologistSpecialty', 'EXTRA_RADIOLOGISTSPECIALTY'),
    ('RadiologistReportDateTime', 'EXTRA_RADIOLOGISTREPORTDATETIME'),
    ('RadiologistFinalisationDate', 'EXTRA_RADIOLOGISTFINALISATIONDATE'),
    ('RadiologistReportDuration', 'EXTRA_RADIOLOGISTREPORTDURATION'),
    ('StaffSignoff', 'EXTRA_STAFFSIGNOFF'),
    ('CollectionTime', 'EXTRA_COLLECTIONTIME'),
    ('SampleReceivedTime', 'EXTRA_SAMPLERECEIVEDTIME'),
    ('TestResult', 'TESTRESULT'),
    ('SignatureDateTime', 'EXTRA_SIGNATUREDATETIME'),
    ('PathologistName', 'EXTRA_PATHOLOGISTNAME'),
    ('PathologistLicence', 'EXTRA_PATHOLOGISTLICENCE'),
    ('ServiceGroupDesc', 'EXTRA_SERVICEGROUPDESC'),
    ('DIN', 'EXTRA_DIN'),
    ('StartDispenseTime', 'EXTRA_STARTDISPENSETIME'),
    ('PrescriptionValidationTime', 'EXTRA_PRESCRIPTIONVALIDATIONTIME'),
    ('QuantityAdministered', 'EXTRA_QUANTITYADMINISTERED'),
    ('QuantityPrescribed', 'EXTRA_QUANTITYPRESCRIBED'),
    ('ProcedureSpecialty', 'EXTRA_PROCEDURESPECIALTY'),
    ('ElectiveOrEmergency', 'EXTRA_ELECTIVEOREMERGENCY'),
    ('PreOpStart', 'EXTRA_PREOPSTART'),
    ('PreOpEnd', 'EXTRA_PREOPEND'),
    ('AnaethesiaStart', 'EXTRA_ANAETHESIASTART'),
    ('AnaethesiaEnd', 'EXTRA_ANAETHESIAEND'),
    ('RecoveryStart', 'EXTRA_RECOVERYSTART'),
    ('RecoveryEnd', 'EXTRA_RECOVERYEND'),
    ('NumberXtraMedicalStaff', 'EXTRA_NUMBERXTRAMEDICALSTAFF'),
    ('NumberExtraPersons', 'EXTRA_NUMBEREXTRAPERSONS'),
    ('NumberTheatreNurses', 'EXTRA_NUMBERTHEATRENURSES'),
    ('NumberTheatreNursesAux', 'EXTRA_NUMBERTHEATRENURSESAUX'),
    ('OncologyFlag', 'EXTRA_ONCOLOGYFLAG'),
    ('PatientType', 'EXTRA_PATIENTTYPE'),
    ('CancellationReasonCode', 'EXTRA_CANCELLATIONREASONCODE'),
    ('CancellationReasonDesc', 'EXTRA_CANCELLATIONREASONDESC'),
    ('AnaesthetistCode', 'EXTRA_ANAESTHETISTCODE'),
    ('AnaesthetistName', 'EXTRA_ANAESTHETISTNAME'),
    ('AnaestheticTechnique', 'EXTRA_ANAESTHETICTECHNIQUE'),
    ('RequestStatus', 'EXTRA_REQUESTSTATUS'),
    ('PlannedSurgeryDate', 'EXTRA_PLANNEDSURGERYDATE'),
    ('OperationID', 'EXTRA_OPERATIONID'),
    ('OperationStatus', 'EXTRA_OPERATIONSTATUS'),
    ('EncounterType', 'ENCOUNTERTYPE'),
    ('PACUDuration', 'EXTRA_PACUDURATION'),
    ('Implants', 'EXTRA_IMPLANTS'),
    ('TestName', 'EXTRA_TESTNAME'),
    ('OrderingConsultant', 'EXTRA_ORDERINGCONSULTANT'),
    ('OrderingConsultantSpecialty', 'EXTRA_ORDERINGCONSULTANTSPECIALTY');






CREATE TABLE FileTypeMapping (
    FileType VARCHAR(255),
    FieldMappingID INT,
    PRIMARY KEY (FileType, FieldMappingID),
    FOREIGN KEY(FieldMappingID) REFERENCES FieldMapping(ID)
);

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'MRN Number' AND FieldOutputField = 'PATIENTNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'Hospital' AND FieldOutputField = 'EXTRA_HOSPITAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'DateOfBirth' AND FieldOutputField = 'DATEOFBIRTH';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'Gender' AND FieldOutputField = 'GENDER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'PatientDeceased' AND FieldOutputField = 'EXTRA_PATIENTDECEASED';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'DateofDeath' AND FieldOutputField = 'EXTRA_DATEOFDEATH';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'PlaceOfBirth' AND FieldOutputField = 'EXTRA_PLACEOFBIRTH';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'EthnicOrigin' AND FieldOutputField = 'ETHNICORIGIN';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'Nationality' AND FieldOutputField = 'EXTRA_NATIONALITY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'LastName' AND FieldOutputField = 'LASTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'FirstName' AND FieldOutputField = 'FIRSTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'Title' AND FieldOutputField = 'TITLE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'MothersName' AND FieldOutputField = 'EXTRA_MOTHERSLASTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'MothersPreName' AND FieldOutputField = 'EXTRA_MOTHERSFIRSTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'FathersName' AND FieldOutputField = 'EXTRA_FATHERSLASTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'FathersPreName' AND FieldOutputField = 'EXTRA_FATHERSFIRSTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'FamilyDoctor' AND FieldOutputField = 'EXTRA_FAMILYDOCTOR';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'BloodRefusal' AND FieldOutputField = 'EXTRA_BLOODREFUSAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'OrganDonor' AND FieldOutputField = 'EXTRA_ORGANDONOR';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'PrefLanguage' AND FieldOutputField = 'EXTRA_PREFLANGUAGE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'LastUpdateDateTime' AND FieldOutputField = 'EXTRA_LASTUPDATEDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Patient ', ID FROM FieldMapping WHERE FileInputField = 'NationalID' AND FieldOutputField = 'NATIONALIDENTIFIER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'SourcePatientNumber' AND FieldOutputField = 'PATIENTNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'Hospital' AND FieldOutputField = 'EXTRA_HOSPITAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'StartDateTime' AND FieldOutputField = 'STARTDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'EndDateTime' AND FieldOutputField = 'ENDDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'EncounterNumber' AND FieldOutputField = 'ENCOUNTERNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'Age' AND FieldOutputField = 'AGE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'EnounterType' AND FieldOutputField = 'ENOUNTERTYPE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'EncounterCategory' AND FieldOutputField = 'ENCOUNTERCATEGORY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'LengthOfStay' AND FieldOutputField = 'LENGTHOFSTAY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AdmitWard' AND FieldOutputField = 'ADMITWARD';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DischargeWard' AND FieldOutputField = 'DISCHARGEWARD';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'ReferringConsultant' AND FieldOutputField = 'REFERRINGCONSULTANT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'ReferringConsultantName' AND FieldOutputField = 'EXTRA_REFERRINGCONSULTANTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'ReferringConsultantSpecialty' AND FieldOutputField = 'REFERRINGCONSULTANTSPECIALTY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AdmittingConsultant' AND FieldOutputField = 'ADMITTINGCONSULTANT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AdmittingConsultantName' AND FieldOutputField = 'EXTRA_ADMITTINGCONSULTANTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AdmittingConsultantSpecialty' AND FieldOutputField = 'ADMITTINGCONSULTANTSPECIALTY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AttendingConsultant' AND FieldOutputField = 'ATTENDINGCONSULTANT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AttendingConsultantName' AND FieldOutputField = 'EXTRA_ATTENDINGCONSULTANTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AttendingConsultantSpecialty' AND FieldOutputField = 'ATTENDINGCONSULTANTSPECIALTY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DischargeConsultant' AND FieldOutputField = 'DISCHARGECONSULTANT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DischargeConsultantName' AND FieldOutputField = 'EXTRA_DISCHARGECONSULTANTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DischargeConsultantSpecialty' AND FieldOutputField = 'DISCHARGECONSULTANTSPECIALTY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'TransferToHospital' AND FieldOutputField = 'EXTRA_TRANSFERTOHOSPITAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'CauseOfDeath' AND FieldOutputField = 'EXTRA_CAUSEOFDEATH';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'TypeOfDeath' AND FieldOutputField = 'EXTRA_TYPEOFDEATH';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DateofDeath' AND FieldOutputField = 'EXTRA_DATEOFDEATH';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'Autopsy' AND FieldOutputField = 'EXTRA_AUTOPSY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DRG1' AND FieldOutputField = 'DRG1';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DRG1Version' AND FieldOutputField = 'DRG1VERSION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DRGGravity' AND FieldOutputField = 'EXTRA_DRGGRAVITY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'MDC' AND FieldOutputField = 'EXTRA_MDC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'LastUpdateDateTime' AND FieldOutputField = 'EXTRA_LASTUPDATEDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DischargeDestination' AND FieldOutputField = 'DISCHARGEDESTINATION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'Address' AND FieldOutputField = 'ADDRESS';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'PostCode' AND FieldOutputField = 'POSTCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'Municipality' AND FieldOutputField = 'EXTRA_MUNICIPALITY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'Suburb' AND FieldOutputField = 'SUBURB';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'Region' AND FieldOutputField = 'EXTRA_REGION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'Country' AND FieldOutputField = 'EXTRA_COUNTRY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'LivingArrangements' AND FieldOutputField = 'EXTRA_LIVINGARRANGEMENTS';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'MaritalStatus' AND FieldOutputField = 'MARITALSTATUS';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AdmissionCategory' AND FieldOutputField = 'ADMISSIONCATEGORY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AdmissionSource' AND FieldOutputField = 'ADMISSIONSOURCE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'AdmissionElection' AND FieldOutputField = 'ADMISSIONELECTION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'HealthFund' AND FieldOutputField = 'HEALTHFUND';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'FinancialClass' AND FieldOutputField = 'FINANCIALCLASS';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'TransferFromHospital' AND FieldOutputField = 'EXTRA_TRANSFERFROMHOSPITAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'ClinicName' AND FieldOutputField = 'EXTRA_CLINICNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'ClinicSpecialtyCode' AND FieldOutputField = 'EXTRA_CLINICSPECIALTYCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'ClinicSpecialty' AND FieldOutputField = 'EXTRA_CLINICSPECIALTY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'ModeOfArrival' AND FieldOutputField = 'EXTRA_MODEOFARRIVAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'PreTriageTime' AND FieldOutputField = 'EXTRA_PRETRIAGETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'TriageStartTime' AND FieldOutputField = 'EXTRA_TRIAGESTARTTIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'TriageEndTime' AND FieldOutputField = 'EXTRA_TRIAGEENDTIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DiagnosisOnDischarge' AND FieldOutputField = 'EXTRA_DIAGNOSISONDISCHARGE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'PhysicianSpecialityKey' AND FieldOutputField = 'EXTRA_PHYSICIANSPECIALITYKEY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'CancellationDate' AND FieldOutputField = 'EXTRA_CANCELLATIONDATE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'CancellationFlag' AND FieldOutputField = 'EXTRA_CANCELLATIONFLAG';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'VisitType' AND FieldOutputField = 'EXTRA_VISITTYPE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'Site' AND FieldOutputField = 'EXTRA_SITE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'DischargeStatus' AND FieldOutputField = 'EXTRA_DISCHARGESTATUS';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'ComplaintDesc' AND FieldOutputField = 'EXTRA_COMPLAINTDESC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'TriageCode' AND FieldOutputField = 'EXTRA_TRIAGECODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Encounter', ID FROM FieldMapping WHERE FileInputField = 'TriageDesc' AND FieldOutputField = 'EXTRA_TRIAGEDESC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'SourcePatientNumber' AND FieldOutputField = 'PATIENTNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'Hospital' AND FieldOutputField = 'EXTRA_HOSPITAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'BedNumber' AND FieldOutputField = 'BEDNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'EncounterNumber' AND FieldOutputField = 'ENCOUNTERNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'Ward' AND FieldOutputField = 'WARD';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'StartDateTime' AND FieldOutputField = 'STARTDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'RoomNumber' AND FieldOutputField = 'EXTRA_ROOMNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'WardType' AND FieldOutputField = 'EXTRA_WARDTYPE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'Leave' AND FieldOutputField = 'LEAVE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'LeaveType' AND FieldOutputField = 'EXTRA_LEAVETYPE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'AttendingConsultant_Code' AND FieldOutputField = 'ATTENDINGCONSULTANT_CODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'AttendingConsultantName' AND FieldOutputField = 'EXTRA_ATTENDINGCONSULTANTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'AttendingConsultant_SpecialtyCode' AND FieldOutputField = 'ATTENDINGCONSULTANT_SPECIALTYCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'LastUpdateDateTime' AND FieldOutputField = 'EXTRA_LASTUPDATEDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Transfer', ID FROM FieldMapping WHERE FileInputField = 'Site' AND FieldOutputField = 'EXTRA_SITE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'SourcePatientNumber' AND FieldOutputField = 'EXTRA_SOURCEPATIENTNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'Hospital' AND FieldOutputField = 'EXTRA_HOSPITAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'EncounterNumber' AND FieldOutputField = 'ENCOUNTERNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'DiagnosisCode' AND FieldOutputField = 'DIAGNOSISCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'DiagnosisVersion' AND FieldOutputField = 'DIAGNOSISVERSION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'Sequence' AND FieldOutputField = 'SEQUENCE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'DiagnosisType' AND FieldOutputField = 'EXTRA_DIAGNOSISTYPE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'ConditionOnset' AND FieldOutputField = 'CONDITIONONSET';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'SequenceService' AND FieldOutputField = 'EXTRA_SEQUENCESERVICE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'PrimaryTumour' AND FieldOutputField = 'EXTRA_PRIMARYTUMOUR';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'TumourCode' AND FieldOutputField = 'EXTRA_TUMOURCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'Metastase' AND FieldOutputField = 'EXTRA_METASTASE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'Ganglion' AND FieldOutputField = 'EXTRA_GANGLION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'StageEvolution' AND FieldOutputField = 'EXTRA_STAGEEVOLUTION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'Morphology' AND FieldOutputField = 'EXTRA_MORPHOLOGY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'Screening' AND FieldOutputField = 'EXTRA_SCREENING';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'DiagnosisDateTime' AND FieldOutputField = 'EXTRA_DIAGNOSISDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'CodeCharacteristic' AND FieldOutputField = 'EXTRA_CODECHARACTERISTIC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'CodeCharacteristicDesc' AND FieldOutputField = 'EXTRA_CODECHARACTERISTICDESC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'LocalDiagCode' AND FieldOutputField = 'EXTRA_LOCALDIAGCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'LocalDiagCodeDesc' AND FieldOutputField = 'EXTRA_DIAGNOSISDESCRIPTION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Diagnosis', ID FROM FieldMapping WHERE FileInputField = 'LastUpdateDateTime' AND FieldOutputField = 'EXTRA_LASTUPDATEDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'SourcePatientNumber' AND FieldOutputField = 'EXTRA_SOURCEPATIENTNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'Hospital' AND FieldOutputField = 'EXTRA_HOSPITAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'EncounterNumber' AND FieldOutputField = 'ENCOUNTERNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'ProcedureDateTime' AND FieldOutputField = 'PROCEDUREDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'ProcedureCode' AND FieldOutputField = 'PROCEDURECODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'ProcedureVersion' AND FieldOutputField = 'PROCEDUREVERSION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'Sequence' AND FieldOutputField = 'SEQUENCE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'InterventionType' AND FieldOutputField = 'EXTRA_INTERVENTIONTYPE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'Consultant' AND FieldOutputField = 'CONSULTANT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'ConsultantName' AND FieldOutputField = 'EXTRA_CONSULTANTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'ConsultantSpecialty' AND FieldOutputField = 'CONSULTANTSPECIALTY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'ProcedureTheatre' AND FieldOutputField = 'PROCEDURETHEATRE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'LocalProcTheatre' AND FieldOutputField = 'EXTRA_LOCALPROCTHEATRE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'LocalProcTheatreDesc' AND FieldOutputField = 'EXTRA_LOCALPROCTHEATREDESC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'NbrProcedures' AND FieldOutputField = 'EXTRA_NBRPROCEDURES';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Procedure', ID FROM FieldMapping WHERE FileInputField = 'LastUpdateDateTime' AND FieldOutputField = 'EXTRA_LASTUPDATEDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'SourcePatientNumber' AND FieldOutputField = 'PATIENTNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'Hospital' AND FieldOutputField = 'HOSPITAL';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'StartDateTime' AND FieldOutputField = 'STARTDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'Quantity' AND FieldOutputField = 'QUANTITY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ServiceCode' AND FieldOutputField = 'SERVICECODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PrimaryProcedure' AND FieldOutputField = 'EXTRA_PRIMARYPROCEDURE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'EncounterNumber' AND FieldOutputField = 'ENCOUNTERNUMBER';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ServicingDepartment' AND FieldOutputField = 'SERVICINGDEPARTMENT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'Duration' AND FieldOutputField = 'DURATION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ActualCharge' AND FieldOutputField = 'ACTUALCHARGE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'EndDateTime' AND FieldOutputField = 'ENDDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PointOfService1' AND FieldOutputField = 'POINTOFSERVICE1';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ServiceDescription' AND FieldOutputField = 'EXTRA_SERVICEDESCRIPTION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ServiceGroup' AND FieldOutputField = 'EXTRA_SERVICEGROUP';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'LastUpdateDateTime' AND FieldOutputField = 'EXTRA_LASTUPDATEDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'Consultant' AND FieldOutputField = 'CONSULTANT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ConsultantName' AND FieldOutputField = 'EXTRA_CONSULTANTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ConsultantSpecialty' AND FieldOutputField = 'CONSULTANTSPECIALTY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'Clinic' AND FieldOutputField = 'CLINIC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OrderDateTime' AND FieldOutputField = 'ORDERDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PriorityCode' AND FieldOutputField = 'EXTRA_PRIORITYCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'Priority' AND FieldOutputField = 'EXTRA_PRIORITY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'StatusCode' AND FieldOutputField = 'EXTRA_STATUSCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'StartDateTreatmentPlan' AND FieldOutputField = 'EXTRA_STARTDATETREATMENTPLAN';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'EndDateTreatmentPlan' AND FieldOutputField = 'EXTRA_ENDDATETREATMENTPLAN';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RequestNo' AND FieldOutputField = 'EXTRA_REQUESTNO';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OrderingDepartment' AND FieldOutputField = 'EXTRA_ORDERINGDEPARTMENT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PrivateInsurance' AND FieldOutputField = 'EXTRA_PRIVATEINSURANCE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OriginalServiceCode' AND FieldOutputField = 'EXTRA_ORIGINALSERVICECODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OriginalServiceDesc' AND FieldOutputField = 'EXTRA_ORIGINALSERVICEDESC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OriginalServiceGroup' AND FieldOutputField = 'EXTRA_ORIGINALSERVICEGROUP';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RadiographerExamDuration' AND FieldOutputField = 'EXTRA_RADIOGRAPHEREXAMDURATION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RadiologistLicence' AND FieldOutputField = 'EXTRA_RADIOLOGISTLICENCE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RadiologistName' AND FieldOutputField = 'EXTRA_RADIOLOGISTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RadiologistSpecialty' AND FieldOutputField = 'EXTRA_RADIOLOGISTSPECIALTY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RadiologistReportDateTime' AND FieldOutputField = 'EXTRA_RADIOLOGISTREPORTDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RadiologistFinalisationDate' AND FieldOutputField = 'EXTRA_RADIOLOGISTFINALISATIONDATE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RadiologistReportDuration' AND FieldOutputField = 'EXTRA_RADIOLOGISTREPORTDURATION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'StaffSignoff' AND FieldOutputField = 'EXTRA_STAFFSIGNOFF';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'CollectionTime' AND FieldOutputField = 'EXTRA_COLLECTIONTIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'SampleReceivedTime' AND FieldOutputField = 'EXTRA_SAMPLERECEIVEDTIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'TestResult' AND FieldOutputField = 'TESTRESULT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'SignatureDateTime' AND FieldOutputField = 'EXTRA_SIGNATUREDATETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PathologistName' AND FieldOutputField = 'EXTRA_PATHOLOGISTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PathologistLicence' AND FieldOutputField = 'EXTRA_PATHOLOGISTLICENCE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ServiceGroupDesc' AND FieldOutputField = 'EXTRA_SERVICEGROUPDESC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'DIN' AND FieldOutputField = 'EXTRA_DIN';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'StartDispenseTime' AND FieldOutputField = 'EXTRA_STARTDISPENSETIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PrescriptionValidationTime' AND FieldOutputField = 'EXTRA_PRESCRIPTIONVALIDATIONTIME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'QuantityAdministered' AND FieldOutputField = 'EXTRA_QUANTITYADMINISTERED';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'QuantityPrescribed' AND FieldOutputField = 'EXTRA_QUANTITYPRESCRIBED';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ProcedureSpecialty' AND FieldOutputField = 'EXTRA_PROCEDURESPECIALTY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'ElectiveOrEmergency' AND FieldOutputField = 'EXTRA_ELECTIVEOREMERGENCY';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PreOpStart' AND FieldOutputField = 'EXTRA_PREOPSTART';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PreOpEnd' AND FieldOutputField = 'EXTRA_PREOPEND';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'AnaethesiaStart' AND FieldOutputField = 'EXTRA_ANAETHESIASTART';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'AnaethesiaEnd' AND FieldOutputField = 'EXTRA_ANAETHESIAEND';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RecoveryStart' AND FieldOutputField = 'EXTRA_RECOVERYSTART';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RecoveryEnd' AND FieldOutputField = 'EXTRA_RECOVERYEND';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'NumberXtraMedicalStaff' AND FieldOutputField = 'EXTRA_NUMBERXTRAMEDICALSTAFF';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'NumberExtraPersons' AND FieldOutputField = 'EXTRA_NUMBEREXTRAPERSONS';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'NumberTheatreNurses' AND FieldOutputField = 'EXTRA_NUMBERTHEATRENURSES';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'NumberTheatreNursesAux' AND FieldOutputField = 'EXTRA_NUMBERTHEATRENURSESAUX';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OncologyFlag' AND FieldOutputField = 'EXTRA_ONCOLOGYFLAG';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PatientType' AND FieldOutputField = 'EXTRA_PATIENTTYPE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'CancellationDate' AND FieldOutputField = 'EXTRA_CANCELLATIONDATE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'CancellationReasonCode' AND FieldOutputField = 'EXTRA_CANCELLATIONREASONCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'CancellationReasonDesc' AND FieldOutputField = 'EXTRA_CANCELLATIONREASONDESC';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'AnaesthetistCode' AND FieldOutputField = 'EXTRA_ANAESTHETISTCODE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'AnaesthetistName' AND FieldOutputField = 'EXTRA_ANAESTHETISTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'AnaestheticTechnique' AND FieldOutputField = 'EXTRA_ANAESTHETICTECHNIQUE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'RequestStatus' AND FieldOutputField = 'EXTRA_REQUESTSTATUS';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PlannedSurgeryDate' AND FieldOutputField = 'EXTRA_PLANNEDSURGERYDATE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OperationID' AND FieldOutputField = 'EXTRA_OPERATIONID';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OperationStatus' AND FieldOutputField = 'EXTRA_OPERATIONSTATUS';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'EncounterType' AND FieldOutputField = 'ENCOUNTERTYPE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'PACUDuration' AND FieldOutputField = 'EXTRA_PACUDURATION';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'Implants' AND FieldOutputField = 'EXTRA_IMPLANTS';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'Site' AND FieldOutputField = 'EXTRA_SITE';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'TestName' AND FieldOutputField = 'EXTRA_TESTNAME';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OrderingConsultant' AND FieldOutputField = 'EXTRA_ORDERINGCONSULTANT';

INSERT INTO FileTypeMapping (FileType, FieldMappingID)
SELECT 'Service', ID FROM FieldMapping WHERE FileInputField = 'OrderingConsultantSpecialty' AND FieldOutputField = 'EXTRA_ORDERINGCONSULTANTSPECIALTY';


CREATE TABLE FieldMapping (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    TypeFichier VARCHAR(255),
    MandatoryField JSON
);

INSERT INTO fichierType (TypeFichier)
VALUES
    ('Patient'),
    ('Diagnosis'),
    ('Encounter'),
    ('Procedure'),
    ('Service'),
    ('Transfer');
