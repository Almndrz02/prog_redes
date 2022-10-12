'''
Descripción: Problema 1 Raíces de la ecuación cuadrática
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''
# se daran valores si estos valores tienes raices se iprimira el mensaje "tiene raices imaginarias"
import math
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
form=b*b-4*a*c
if(a!=0):
 if(form<0):
  print("tiene raices imaginarias")
 else:
  x1=(-b+(math.sqrt(form)))/(2*a)    # si no se realizara una operacion y nos imprimira no tiene solucion 
  x2=(-b-(math.sqrt(form)))/(2*a)
  print("X1 = "+str(x1)+" X2 = "+str(x2))
else:
 print("No tiene solucion")
 