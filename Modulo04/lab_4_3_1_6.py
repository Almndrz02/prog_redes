'''
Descripción: Un año bisiesto: escribiendo tus propias funciones
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''

def is_year_leap(year):
    
	if year % 4 != 0: # estamos comprobando si el año es bisisesto 
		return False
	elif year % 100 != 0: # como se puede ver esta fucion se repite 
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

test_data = [1900, 2000, 2016, 1987]      
test_results = [False, True, True, False]
for i in range(len(test_data)):     # se realizo un ciclo para ver si es bicicesto 
	yr = test_data[i]               # y asi se pueda imprimir en pantalla
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")