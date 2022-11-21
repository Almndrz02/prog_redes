'''
Nombre del api: The Rick and Morty API
Descrpcion del API: Obenten informacion de personajes de la serie animada rick and morty
pudiendo mostrar informacion como nombre, estado y especie. 
API portal: https://rickandmortyapi.com/ 
Autor: Daniel Almendariz
Fecha: 14 Nov 2022
'''

import urllib.parse
import requests

main_api = "https://rickandmortyapi.com/api/character/420"


data = requests.get(main_api)
if data.status_code == 200:
        data = data.json()
        for e in data['character']:
            print("Nombre: "+(e['nombre']))
            print("Estatus: "+(e['status']))
            print("Especie: "+(e['specie']))
            
        
        
        
        