# TER_ETL_Donnne_Clinique
from java.text import SimpleDateFormat
from java.util import Date, Calendar

flowFile = session.get()

if flowFile is not None:
    # Get an attribute
    dob_str = flowFile.getAttribute('DateOfBirth')
    dob_format = SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss zzz")
    dob = dob_format.parse(dob_str)

    # Get today's date and subtract 125 years
    now = Calendar.getInstance()
    now.add(Calendar.YEAR, -125)




    # Check if dob is less than 125 years ago
    if dob.before(now.getTime()):
        session.transfer(flowFile, REL_FAILURE)
    else:
		session.transfer(flowFile, REL_SUCCESS)