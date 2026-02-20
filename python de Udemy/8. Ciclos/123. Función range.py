"""
Docstring for python de Udemy.8. Ciclos.123. Función range

Funcion range

la funcion range es una funcion incorporada que geenra una secuencia de numeros

Es comunmente utilizada para itera sobre siclos tipo for

syntaxis funcion range
# incio - valor inicial (opcional)
# fin - valor final, sin incluirlo
# incremento - diferencia entre cad numero opcional
"""

print("**** Funciion range ***")

print("\nSecuencia del 0 al 4")
# inicio = 0
# fin = 5 - 1 =4
# Incrementeo = 1 (opcional)
for i in range(5): # fin 5 - 1
    print(i, end=" ")

print("\n\nSecuencie dle 10 al 20")
# inicio = 10
# fin = 21 - 1 = 20
# incremente = 1 (opcional)
for i in range(10, 20 + 1):
    print(i, end=" ")

print("\n\nSecuencie dle 20 al 30")
# inicio = 10
# fin = 21 - 1 = 20
# incremente = 1 (opcional)
for i in range(20, 30 + 1, 2):
    print(i, end=" ")

