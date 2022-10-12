'''
Descripción: Problema 2 Número divisible entre otro
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''

# nos pedira ingresar dos valores 
numero1=int(input("Numero1: "))
numero2=int(input("Numero2: "))

resto=numero1%numero2 # realizara una opercion para ver si estos valores son divisibles 

con= resto == 0
print("¿", numero1,"es divisible entre",numero2,"?",con)   # si los valores son divisibles nos dira True si no False