print("IMPORTACION Y CREACION DE MODULOS")
print("En Python, un módulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas. La importación de módulos nos permite acceder a la funcionalidad definida en otros archivos y reutilizar código de manera eficiente. Además, podemos crear nuestros propios módulos para organizar y modularizar nuestro código.")

print("")

print("Ten en cuenta")
print("Python viene con una amplia biblioteca estándar de módulos que proporcionan funcionalidades adicionales. Estos módulos están disponibles sin necesidad de instalarlos por separado.")

print("")

print("Importar módulos")
print("Para utilizar un módulo en nuestro programa, debemos importarlo utilizando la declaración import. Podemos importar un módulo completo o funciones específicas de un módulo.")

import math

resultado = math.sqrt(25)
print(resultado) # Imprime 5.0

print("En este ejemplo, se importa el módulo math utilizando la declaración import. Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25.")
print("")
print("También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función.")
print("")

from math import sqrt

result = sqrt(25)
print(resultado) # Imprime 5

print("En este caso, se importa solo la función sqrt() del módulo math, lo que nos permite utilizarla directamente sin tener que precederla con el nombre del módulo.")

print("")

print("FUNCIONES Y CLASES DE MÓDULOS ESTÁNDAR")
print("La biblioteca estándar de Python ofrece una amplia gama de módulos con funciones y clases útiles. Algunos ejemplos comunes incluyen:")

print("")

print("La funcion math proporciona funciones matematicas como sqrt() (raiz cuadrada), sin() (seno), cos() (coseno), entre otras.")

print("")

print("La funcion random Ofrece funciones para generar números aleatorios, como random() (número aleatorio entre 0 y 1), randint() (número entero aleatorio en un rango), entre otras.")

print("")

print("La funcion Datetime Permite trabajar con fechas y horas, como datetime.now() (fecha y hora actual), datetime.date() (fecha), datetime.time() (hora), entre otras.")

print("")

import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio) # Imprime un numero entero aleatorio entre 1 y 10

import datetime

fecha_actual = datetime.datetime.now()
print(fecha_actual) # Imprime la fecha y hora actual

from datetime import datetime # Import correcto (mas simple)

fecha_actual = datetime.now() #¡agrega los parentesis!

print("")

print("Estos son solo algunos ejemplos de los muchos módulos disponibles en la biblioteca estándar de Python. Puedes consultar la documentación oficial de Python para obtener más información sobre los módulos y sus funcionalidades.")


