from zeep import Client
import json
from datetime import datetime, timedelta

# URL to the WSDL file describing the SOAP service
wsdl_url = 'https://api.timeteccloud.com/webservice/WebServiceTimeTecAPI.asmx?WSDL'

# Create a SOAP client
client = Client(wsdl_url)

# Construct the SOAP header
header = {
    'WebServiceSoapHeader': {
        'WSUsername': 'qatarproject@timetecqatar.com',
        'WSPassword': 'ICwiSA3RPQ4cEP3AUNG1Vw8mI6EN5jZF72fxlFztWbJ1EWJ114',
        'SecurityToken': 'F0E6DDD087C520725A3B6A3DFF8AAC5D428F3F0B'
    }
}

# Construct the SOAP request
request_data = {
    'CompanyID': '8953',
    'UserID': '100100',
    'CheckTimeFrom': '2023-12-28',
    'CheckTimeTo': '2023-12-28',
    'RecordStartFrom': '',
    'LimitRecordShow': ''
}

# Send the SOAP request with the header
response = client.service.GetAttendance(_soapheaders=header, **request_data)

# Handle the SOAP response
response_dict = json.loads(response)

Obj = response_dict['Result']['AttendanceObj']

result = Obj[0]

date = result['Date']
in_time = result['In']
out_time = result['Out']
division = result['Division']
User_ID = result['User_ID']
print("Start of API Result")
print(f"User_ID: {User_ID}")
print(f"Date: {date}")
print(f"In time: {in_time}")
print(f"Out time: {out_time}")
print(f"Divison: {division}")
print("End of API Result")
date_time_in = datetime.strptime(f"{date} {in_time}", "%d/%m/%Y %H:%M")

result_utc_in = date_time_in.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'

print(f"Original IN Date and Time: {date_time_in}")
print(f"Result in UTC Format: {result_utc_in}")

date_time_out = datetime.strptime(f"{date} {out_time}", "%d/%m/%Y %H:%M")

result_utc_out = date_time_out.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'

print(f"Original OUT Date and Time: {date_time_out}")
print(f"Result in UTC Format: {result_utc_out}")

in_obj = {
    "userCode": User_ID,
    "entryDate": result_utc_in,
    "entryCode": "IN",
    "readerDescription": division
}
out_obj = {
    "userCode": User_ID,
    "entryDate": result_utc_out,
    "entryCode": "OUT",
    "readerDescription": division
}
arr_obj = []
arr_obj.append(in_obj)
arr_obj.append(out_obj)
for object in arr_obj:
    print(object)