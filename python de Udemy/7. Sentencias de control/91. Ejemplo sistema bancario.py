"""
Docstring for python de Udemy.7. Sentencias de control.91. Ejemplo sistema bancario

SISTEMA BANCARIO

Considerando que estamos dentro de un sistema bancario, se solicita preguntar al usuario si desea continuar dentro del sistema.

Utilizando el operador not para aplicar una logica inversa se debe programar las siguientes condiciones:

- Si NO deseamos salir del sistema, impremir:
    Continuamos dentro del sistema...

- De lo contrario, imprimimos:
    Saliendo del sistema
"""

print("*** BIENVENDIOS AL SISTEMA BANCARIO ***")

salir_sistema_txt = input("Desea salir del sistema (si/no)? ")
salir_sistema = salir_sistema_txt.strip().lower() == "si"

if not salir_sistema:
    print("continuamos dentro del sistema")
else:
    print("Salimos del sistema")