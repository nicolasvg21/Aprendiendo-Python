"""
Docstring for python de Udemy.7. Sentencias de control.88. Ejemplo valor positivo
"""
print("*** REVISAR SI EL NUMERO ES POSITIVO ***")
numero = int(input("escribe un numero:"))

if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero < 0:
    print(f"el numero {numero} es negativo")
else:
    print(f"El numero es {numero} entonces es igual a 0")