'''
Descripción: El Feo Devorador de Vocales
Autor: Daniel Almendariz
Fecha: 29 sep 2022
'''

userWord=input("Ingresa una palabra: ")
UserWord=userWord.upper()

for letra in userWord:
    if letra=='A':
        continue
    elif letra=='E':
        continue
    elif letra=='I':
        continue
    elif letra=='O':
        continue 
    elif letra=='U':
        continue 
    else:
        print (letra)
