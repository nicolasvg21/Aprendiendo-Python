"""
Docstring for python de Udemy.6. Operadores.76. Valor dentro del rango

VALOR DENTRO DEL RANGO

solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado está dentro del rango 

Se deben definir 2 constante, VAOR_MINIMO = 0 Y VALOR_MMAXIMO = 5

Y debemos comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5

Finalmente se debe imprimir:
Valor dentro del rango: True / False
"""

print("***** valor dentro del rango *****")

VALOR_MINIMO = 0 
VALOR_MAXIMO = 5

valor_usuario = int(input("escribe un numero entre 0 y 5: "))

resultado1 = valor_usuario >= VALOR_MINIMO and valor_usuario <= VALOR_MAXIMO
resultado2 = VALOR_MINIMO <= valor_usuario <= VALOR_MAXIMO
print(resultado1)
print(resultado2)