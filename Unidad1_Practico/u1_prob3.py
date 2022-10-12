'''
Descripción: Problema 3 Secuencia de números enteros
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''
# ingresar un numero y el ciclo realizara una cuenta regresiva 
a = int(input("Ingresa un número: "))
for i in range(a, -1, -1):
    print(i, end=", ")