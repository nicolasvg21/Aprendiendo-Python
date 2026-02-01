"""
Tipos de datos

- int que pertenecen a los numeros enteros sin decimales
- float o flotantes con decimales
- strings que son cadenas de texto entre ""
- bool o booleanos son del tipo logico que solo arrojan verdadero o falso
"""

#1. Enteros (int): Numeros exactos sin decimales
vidas_jugaor = 3
puntos_totales = 1500

#2. Flotantes (float): Numeros con precision decimal
precio = 19.99
pi = 3.14
temperatur = 5.5

#Ojo: 10 es int, pero 10.0 es float

#3. Strings (str): Secuencia de caracteres
#Siempre van entre comillas (dobles o simpes)

curso = "curso de python"
nivel = 'principiante'
#Esto es texto, No unumero c(como un codigo postal):
codigo_postal = '28013'

# print(codigo_postal + 5) -> error!

#4. Booleandos (bool): Interruptores lógcos
#Solo exiten dos valores posibles
#La primera legtra debe ser mayuscula

es_divertido = True
Está_lloviendo = False

fame_over = False
usuario_logueado = True

# La famosa FUNCION TYPE()
#¿No estás seguro del tipo de un dato?
# ¡preguntales a python!

x = 10
y = '10'

print(type(x)) # Salida:
print(type(y)) # Salida:

# Es muy util para depurar errores.