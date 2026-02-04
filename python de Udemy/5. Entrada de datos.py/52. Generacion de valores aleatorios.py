"""
Docstring for python de Udemy.5. Entrada de datos.py.52. Generacion de valores aleatorios

La funcion randint(), que es parte de modulo "random", nos permite generar numeros aleatorios

randint(a, b) devuelve un numero aleatorio entre a y b, incluuyendo estos valores.

Es necesario importar en primer lugar el módulo random antes de usar la funcion randint

Para importar un módulo, usamos la sintaxis: 
import random
"""
import random

#import rangom
from random import randint

# Generar un numero aleatorio entre 1 y 10
numero = randint(1, 10)
print(f"Numero aleatorio entre 1 y 10: {numero}")

# Simular un dado de 6 caras
dado = randint(1,6)
print(f"Resultado de lanzar el dado: {dado}")

#----------------------------------------------

import random
#sin colocar from random import randint
numero = random.randint(1,10)

