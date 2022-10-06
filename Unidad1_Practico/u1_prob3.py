'''
Descripción: Problema 3 Secuencia de números enteros
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")