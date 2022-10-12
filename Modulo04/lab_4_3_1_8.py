'''
Descripción: Día del año: escribiendo y utilizando tus propias funciones
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''

def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):   # esta tomando en cnuenta los dias que tiene un mes 
		md = daysInMonth(year, m)
		if md == None:
			return None # verifica el dia para poder enviarlo a la pantalla
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day    # suma todos los dias y los envia a imprimir a pantalla 
	else:
		return None

print(dayOfYear(2000, 12, 31))
