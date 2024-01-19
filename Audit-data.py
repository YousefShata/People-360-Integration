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
    'UserID': '11111',
    'CheckTimeFrom': '2024-1-9',
    'CheckTimeTo': '2024-1-9',
    'RecordStartFrom': '',
    'LimitRecordShow': ''
}

# Send the SOAP request with the header
response = client.service.GetAuditData(_soapheaders=header, **request_data)

# Handle the SOAP response
response_dict = json.loads(response)

Obj = response_dict['Result']['AuditDataObj']



for result in Obj:
    for key, value in result.items():
        if key == "CheckType":
            if value == '0':
                Clockin = Obj[0]
            elif value == '1':
                Clockout = result
                
if Clockout:
    print(f"Clockout: {Clockout}")
else:
    print("No result found with the specified conditions.")

if Clockin:
    print(f"Clockin: {Clockin}")
else:
    print("No result found with the specified conditions.")

print("Done")