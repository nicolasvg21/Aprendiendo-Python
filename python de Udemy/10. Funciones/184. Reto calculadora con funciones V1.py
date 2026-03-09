"""
Calculadora (con funciones)

Crear un programa para agregar las operaciones basicas de una calculadora.

Las opreaciones que debe poder realizar son:

1. Sumar
2. Restar
3. Multiplicar
4. Dividir

Se debe agregar un menu para mostrar cada opcion
"""
print("Reto Calculadora")

def funcion_suma(a, b):
    # pass
    resultado = a + b
    return resultado

def funcion_resta(a, b):
    # pass
    resultado = a - b
    return resultado

def funcion_multiplicar(a, b):
    #pass
    resultado = a * b
    return resultado

def funcion_division(a, b):
    # pass
    resultado = a / b
    return resultado

if __name__ == "__main__":
    while True:
        print("""\n---- Menú -----
        1. Sumaar
        2. Restar
        3. Multiplciar
        4. Dividir""")

        opcion = int(input("\nEscoge una opción del 1 - 5: "))
        if opcion == 1:
            print("Sumar a + b")
            a = int(input("Ingresa el valor de a: "))
            b = int(input("Ingresa el valor de b: "))
            resultado = funcion_suma(a, b)
            print(f"{'='*40}")
            print(f"Resultado de la funcion {resultado}")
            print(f"{'='*40}")

        elif opcion == 2:
            print("Restar a - b")
            a = int(input("Ingresa el valor de a: "))
            b = int(input("Ingresa el valor de b: "))
            resultado = funcion_resta(a, b)
            print(f"{'='*40}")
            print(f"Resultado de la funcion {resultado}")
            print(f"{'='*40}")

        elif opcion == 3:
            print("Multiplicar a * b")
            a = int(input("Ingresa el valor de a: "))
            b = int(input("Ingresa el valor de b: "))
            resultado = funcion_multiplicar(a, b)
            print(f"{'='*40}")
            print(f"Resultado de la funcion {resultado}")
            print(f"{'='*40}")

        elif opcion == 4:
            print("Dividir a / b")
            a = int(input("Ingresa el valor de a: "))
            b = int(input("Ingresa el valor de b: "))
            resultado = funcion_division(a, b)
            print(f"{'='*40}")
            print(f"Resultado de la funcion {resultado}")
            print(f"{'='*40}")

        elif opcion == 5:
            print("\nLograste salir con exito!")
            break

        else:
            print("\nError, la opcion seleccionada es invalida!")