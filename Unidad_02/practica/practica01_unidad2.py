'''
Descripción: Se realizara un programa con API para
             solicitar un nombre y un author
Autor: Daniel Almendariz
Fecha: 08 Nov 2022
'''

import urllib.parse
import requests

main_api = "https://newsapi.org/v2/top-headlines?"
key  = "fd4e84b47b9940609fa13b6a984173e3"

#este ciclo while esta solicitando los datos al usuario de esa misma manera puedes cancelar ingresar los datos
while True:
    sources= input("sources: ") #ingrese bbc-news
    if sources == "salir" or sources== "s": 
        break
    
    print
    
    url = main_api + urllib.parse.urlencode({ "sources":sources, "apikey": key})
    print("URL: " + (url)) # crea el url de donde saca la informacion de api

    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        for e in data['articles']:
            print("title: "+(e['title']))
            print("descripcion: "+(e['description']))
            print("url: "+(e['url']))
            print("publishedAt: "+(e['publishedAt']))
            print("content: "+(e['content']))
        