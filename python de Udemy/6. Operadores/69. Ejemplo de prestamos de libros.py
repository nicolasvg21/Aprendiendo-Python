"""
Docstring for python de Udemy.6. Operadores.69. Ejemplo de prestamos de libros

Sistema prestamos d elibros

Se pide crear un sistema para una biblioteca, la cual desea presta libras si cumple con cualquiera de las siguiente condiciones.

1. El usuario tiene credecniales de estudiante
2. El usuario vive a no mas de 3km a la redonda

si cumple con cualquiera de estas condiciones se le puede presta el libro
"""

print("**** SISTEMA DE PRESTAMOS DE LIBROS *****")

DISTANCIA_PREMITIDA_KM = 3
tiene_credencial = input("cuantas con credencial de destudiante: (si/no) ")
distanci_biblioteca_km = int(input("A cuantos km vives de l abiblioteca? "))

es_elegible_prestamo = (tiene_credencial.strip().lower() == "si" or distanci_biblioteca_km <= DISTANCIA_PREMITIDA_KM)

print(f"Eres elegible para prestamo de libros: {es_elegible_prestamo}")
