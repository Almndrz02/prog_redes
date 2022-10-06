'''
Descripción: Problema 1 Raíces de la ecuación cuadrática
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''

import math
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
form=b*b-4*a*c
if(a!=0):
 if(form<0):
  print("tiene raices imaginarias")
 else:
  x1=(-b+(math.sqrt(form)))/(2*a)
  x2=(-b-(math.sqrt(form)))/(2*a)
  print("X1 = "+str(x1)+" X2 = "+str(x2))
