'''
Descripción:  programa que almacene las asignaturas de un curso
Autor: Daniel Almendariz
Fecha: 11 oct 2022
'''

#Ingresar la calificacion de cada materia
asig1= ["Matemáticas"]
asig2= ["Física"] 
asig3= ["Química"]
asig4= ["Historia"] 
asig5= ["Lengua"]
for i in range(len(asig1)-1, -1, -1):
    nota1 = float(input("¿Qué nota has sacado en " + asig1[i] + "?")) # toma lanota que ingresamos y a la asigna a la metaria
    
for i in range(len(asig2)-1, -1, -1):
    nota2 = float(input("¿Qué nota has sacado en " + asig2[i] + "?"))
    
for i in range(len(asig3)-1, -1, -1):
    nota3 = float(input("¿Qué nota has sacado en " + asig3[i] + "?"))
    
for i in range(len(asig4)-1, -1, -1):
    nota4 = float(input("¿Qué nota has sacado en " + asig4[i] + "?"))
    
for i in range(len(asig5)-1, -1, -1):
    nota5 = float(input("¿Qué nota has sacado en " + asig5[i] + "?"))
    
    # imprime la materia con la nota 
print(asig1, 'has sacado', nota1)
print(asig2, 'has sacado', nota2)
print(asig3, 'has sacado', nota3)
print(asig4, 'has sacado', nota4)
print(asig5, 'has sacado', nota5)




