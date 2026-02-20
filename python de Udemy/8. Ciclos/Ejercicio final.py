"""
Docstring for python de Udemy.8. Ciclos.Ejercicio final

Ejercicio Contador de Vocales en Python
Escribe un programa que declare una variable llamada cadena con el valor de "Hola Mundo".

Posteriormente usando un ciclo for, debe contar la cantidad de vocales presentes en la cadena y finalmente imprimir la cantidad de vocales encontradas (solo el número con la cantidad de vocales encontradas es el que se debe imprimir).

Nota: La salida del programa debe ser idéntico al solicitado, no agregar espacios, textos o saltos de línea innecesarios, de lo contrario la prueba a ejecutar podría fallar.

Instrucciones de Ejecución:

1. Deben presionar el botón de "Ejecutar código" para ver su resultado,

2. Finalmente presionar el botón de "Ejecutar pruebas" para que quede resuelto el ejercicio.

3. Nota: Tu código podría estar correcto, pero recuerda que lo importante es el resultado de ejecutar la prueba, así que revisa nuevamente las instrucciones del ejercicio y respétalas por completo.
"""

palabra = "Hola mundo"      # Declarar la variable
for i in palabra:           # Agregar el ciclo for 
    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
        continue
    print(i, end=" ")
    