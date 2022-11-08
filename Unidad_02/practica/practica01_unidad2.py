'''
Descripción: Se realizara un programa con API para
             solicitar un nombre y un author
Autor: Daniel Almendariz
Fecha: 08 Nov 2022
'''

import urllib.parse
import requests

main_api = "https://newsapi.org/v2/everything?q=Apple&from=2022-11-08&sortBy=popularity&apiKey=fd4e84b47b9940609fa13b6a984173e3"
key  = "fd4e84b47b9940609fa13b6a984173e3"

#este ciclo while true esta solicitando los datos al usuario de esa misma manera puedes cancelar ingresar los datos
while True:
    name = input("Starting Location: ") #Soicita un nombre
    if name == "salir" or name == "s":  #Dedicir si quieres salir
        break
    author = input("Destination: ")  #Solicita el autor
    if author == "salir" or author == "s":
        break

    url = main_api + urllib.parse.urlencode({ "from":name, "to": author, "key": key})
    print("URL: " + (url)) # crea el url de donde saca la informacion de api

    json_data = requests.get(url).json()