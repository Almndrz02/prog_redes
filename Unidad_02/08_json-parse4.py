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