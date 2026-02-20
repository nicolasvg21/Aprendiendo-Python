"""
Docstring for python de Udemy.8. Ciclos.116. Propuesto - calculadora

Aplicacion calculadora

Crear una palicacion de calculador aocn las opciones de:

1. Suar
2. Restar
3. Multiplicar
4. Division

El programa debe mostrar un menu con cada opcion, y debe solicitar los valores de operando 1 y operando 2 para realizar la operación seleccionada.
"""

operación = True
while operación:
    print(""" Menú de opciones
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir""")
    opcion = int(input("\nElige una opción del 1-5 "))
    if opcion == 1:
        print("\nLa operación de suma es de a + b")
        a = float(input("Dale un valor a 'a' "))
        b = float(input("Dale un valor a 'b' "))
        resultado = a + b
        print(f"\nLa operacion quedó como {a} + {b} = {resultado:.2f}")
        print("\nDeseas realizar otra operacion? ")

    elif opcion == 2:
        print("\nLa operación de resta es de a - b")
        a = float(input("Dale un valor a 'a' "))
        b = float(input("Dale un valor a 'b' "))
        resultado = a - b
        print(f"\nLa operacion quedó como {a} - {b} = {resultado:.2f}")
        print("\nDeseas realizar otra operacion? ")

    elif opcion == 3:
        print("\nLa operación de multiplicacion es de a + b")
        a = float(input("Dale un valor a 'a' "))
        b = float(input("Dale un valor a 'b' "))
        resultado = a * b
        print(f"\nLa operacion quedó como {a} * {b} = {resultado:.2f}")
        print("\nDeseas realizar otra operacion? ")

    elif opcion == 4:
        print("\nLa operación de division es de a / b")
        a = float(input("Dale un valor a 'a' "))
        b = float(input("Dale un valor a 'b' "))
        resultado = a / b
        print(f"\nLa operacion quedó como {a} / {b} = {resultado:.2f}")
        print("\nDeseas realizar otra operacion? ")

    elif opcion == 5:
        operación = False
        print("\nHas salido exitosamente vuelve pronto")
    
    else:
        print("\nVea sapo solo tiene 4 opciones de 1-4, escoja una de esas")
else:
    print("\nTerminando la aplicacion de cajero automatico")

    