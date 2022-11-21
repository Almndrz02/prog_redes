'''
Nombre del api: News API
Descrpcion del API:Obtenga y busque noticias de más de 30,000 
publicaciones con esta API simple y gratuita (para proyectos no 
comerciales), puede consultar por palabra clave, publicación o tema.
API portal: https://newsapi.org/ 
Autor: Daniel Almendariz
Fecha: 08 Nov 2022
'''

import urllib.parse
import requests

main_api = "https://newsapi.org/v2/top-headlines?"
key  = "fd4e84b47b9940609fa13b6a984173e3"

#este ciclo while esta solicitando una fuente o un titulo de alguna noticia 
while True:
    sources= input("sources: ") #ingrese bbc-news
    if sources == "salir" or sources== "s": 
        break
    
    print
    
    url = main_api + urllib.parse.urlencode({ "sources":sources, "apikey": key})
    print("URL: " + (url)) # crea el url de donde saca la informacion de api
    
    #toma la infromacion que esta el el api y la muestra en una lista
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        for e in data['articles']:
            print("Title: "+(e['title']))
            print("Descripcion: "+(e['description']))
            print("Url: "+(e['url']))
            print("PublishedAt: "+(e['publishedAt']))
            print("Content: "+(e['content']))
        