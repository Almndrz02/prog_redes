'''
Descripción: Lo esencial del bucle while - Adivina el número secreto
Autor: Daniel Almendariz
Fecha: 27 sep 2022
'''

secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

number = int(input("¿Cuál es el numero secreto?: "))
while number != secret_number:
    print("¡ja, ja! ¡Estás atrpado en mi bucle!")

    number = int(input("Ingresa un numero nuevamente: "))
print("¡Bien hecho, muggle! Eres libre ahora")

