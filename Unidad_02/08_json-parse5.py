'''
Descripción:
Autor: Daniel Almendariz
Fecha: 25 oct 2022
'''

import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?key=XAH6hb1DHGuvudWKtLUid2U1G5DMHrrI&from=Clarendon%20Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA"
key  = "XAH6hb1DHGuvudWKtLUid2U1G5DMHrrI"

while True:
    
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]


    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n") 
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")