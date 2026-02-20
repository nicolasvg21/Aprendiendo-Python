"""
Docstring for python de Udemy.8. Ciclos.107. Ejemplo ciclos while
"""
print("**** Ciclo While ****")

# Imprimir los valoes del 1 al 5
contador = 1
while contador <= 5:
    print(contador, end=" ")
    contador += 1 # Es lo mismo que decir contador = contador + 1

# Si no se agrega el incremento del contador, de va a desarrollar un debug infinito