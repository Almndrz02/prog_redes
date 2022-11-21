'''
Nombre del api: thecocktaildb
Descrpcion del API: Obten inofrmacion sobre coctesles, como cuales son sus ingredientes.  
API portal: https://www.thecocktaildb.com/api.php
Autor: Daniel Almendariz
Fecha: 14 Nov 2022
'''

import urllib.parse
import requests

main_api = "https://www.thecocktaildb.com/api/json/v1/1/search.php?"


#este ciclo while esta solicitando los datos al usuario de esa misma manera puedes cancelar ingresar los datos
while True:
    coctel= input("Coctel: ") #ingresa como ejemplo blue margarita
    if coctel == "salir" or coctel== "s": 
        break
    
    url = main_api + urllib.parse.urlencode({'s': coctel})
    print ("URL: " +(url)) # crea el url de donde saca la informacion sitio del api
    
    #toma la infromacion que esta el el api y la muestra en una lista
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        for e in data['drinks']:
            print("ingredientes: "+(e['strIngredient1']))
            print("ingredientes: "+(e['strIngredient2']))
            print("ingredientes: "+(e['strIngredient3']))
            print("ingredientes: "+(e['strIngredient4']))
            