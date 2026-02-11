"""
Docstring for python de Udemy.7. Sentencias de control.97. El mayor de dos numeros

El mayor de 2 numeros

Crear un programa para indicar cual es el mayor de dos numeros.

El programa deber pedir al usuario dos numeros enteros

Posterormente se debe comprara y mandar a imprimier el numero mayor.
"""

print("---- El mayor de 2 numeros ------")

print("Escribe 2 valores diferentes para a y b")
a = int(input("Asignale un numero entero a 'a' "))
b = int(input("Asignale un numero entero a 'b' "))

if a > b:
    print(f"a es igual a {a}, por ende es mayor que b")
elif a == b:
    print("Maldita sea le digo a y b no puedne tener el mismo valor")
else:
    print(f"b es igual a {b}, por ende es mayor que a")


