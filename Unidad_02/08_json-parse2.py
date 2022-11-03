'''
Descripción:
Autor: Daniel Almendariz
Fecha: 25 oct 2022
'''

import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?key=XAH6hb1DHGuvudWKtLUid2U1G5DMHrrI&from=Clarendon%20Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA"
orig = "Washington"
dest = "Baltimaore"
key  = "XAH6hb1DHGuvudWKtLUid2U1G5DMHrrI"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")