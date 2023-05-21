from convertdate import islamic
from dateutil.parser import parse, ParserError
from datetime import datetime
from convertdate import islamic

def convert_date_format(date_string):
    hijri_year = islamic.from_gregorian(datetime.now().year, datetime.now().month, datetime.now().day)[0]
    if len(date_string) >= 19:
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

data = [ {
  "BIRTHDATE" : "Tue, 28 Jan 1941",
  "PATIENTNUMBER" : "azeazea"
}, {
  "BIRTHDATE" : "03-11-1393",
}, {
  "BIRTHDATE" : "Sat, 22 May 1954 00:00:00 GMT",
}, {
  "BIRTHDATE" : "Thu, 02 Sep 1965 00:00:00 GMT",
}, {
  "BIRTHDATE" : "Mon, 10 Apr 1967 00:00:00 GMT",
}, {
  "BIRTHDATE" : "Sat, 17 Dec 1932 00:00:00 GMT",
}, {
  "BIRTHDATE" : "2012-05-01 00:00:00",
}, {
  "BIRTHDATE" : "2022/10/06 13:45:30",
}, {
  "BIRTHDATE" : "Tue 25",
}, {
  "BIRTHDATE" : "1393/03/11 14:34:56",
}, {
  "BIRTHDATE" : "1941 Jan 28",
}, {
  "BIRTHDATE" : "1965-Sep-2 00:00:00",
}, {
  "BIRTHDATE" : "2022-05-18T16:45:30Z",
}, {
  "BIRTHDATE" : "2022-05-18T11:45:30-05:00",
}]


for item in data:
    if item['BIRTHDATE']:
        item['BIRTHDATE'] = convert_date_format(item['BIRTHDATE'])

for item in data:
    print(item["BIRTHDATE"])  # Print the modified data
    

