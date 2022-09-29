'''
Descripción: Lo básico de las listas
Autor: Daniel Almendariz
Fecha: 29 sep 2022
'''

hat_list = [1, 2, 3, 4, 5]  

userNumber = int(input("Dame un numero para remplazar: "))
hat_list[2] = userNumber

del hat_list[4]

print(len(hat_list))
print(hat_list)