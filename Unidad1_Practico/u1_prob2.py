'''
Descripción: Problema 2 Número divisible entre otro
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''

numero1=int(input("Numero1: "))
numero2=int(input("Numero2: "))

residuo=numero1%numero2

condision= residuo == 0
print("¿", numero1,"es divisible entre",numero2,"?",condision)