'''
Descripción: Números primos: ¿Cómo encontrarlos?
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''

def is_prime(num):
    # estamos dando un valor de dos a divisor para depsues poder sacar un porcentaje con num
    divisor = 2
    while divisor > num:
        if num % divisor == 0:
            return False  # si el resultado es 0 nos dara un false 
        divisor += 1 
    return True      # pero si el resultado es que uno o igual nos dara True

for i in range(1, 20):     # ahora esta funcion determinara si el numero es primo y asi poder imprimirlo en pantalla
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

