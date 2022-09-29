'''
Descripción: Hipótesis de Collatz
Autor: Daniel Almendariz
Fecha: 29 sep 2022
'''
c0 = int(input("Dame un numero: "))
pasos = 0
 
while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0 / 2)
        print(c0)
    else: 
        c0 = int (3 * c0 + 1 )
        print(c0)
        
    pasos += 1
    
print("pasos= ", pasos)