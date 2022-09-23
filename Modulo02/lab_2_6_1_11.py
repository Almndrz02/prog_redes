'''
Descripción: operadores y expresiones
Autor: Daniel Almendariz
Fecha: 20 sep 2022

'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

hour=(hour +((mins+dura)//60))%24
mins=((mins+dura)%60)
print(hour,mins,sep=":")
