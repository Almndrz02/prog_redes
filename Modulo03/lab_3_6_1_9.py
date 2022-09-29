'''
Descripción: Operando con listas - conceptos básicos
Autor: Daniel Almendariz
Fecha: 29 sep 2022
'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

newList = []
for i in my_list:
    if i not in newList:
        newList.append(i)
        
print("La lista con elementos únicos:")
print(newList)
