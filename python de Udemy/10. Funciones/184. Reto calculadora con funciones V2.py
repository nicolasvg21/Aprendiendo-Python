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

def mostrar_menu():
    print("""\n---- Menú -----
    1. Sumaar
    2. Restar
    3. Multiplciar
    4. Dividir
    5. Salir""")
    return int(input("\nEscoge una opción del 1 - 5: "))

def pedir_valores():
    operando1 = float(input("\nDame el valor 1: "))
    operando2 = float(input("Dame el valor 2: "))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):  
    # Solitictar los valores de los operandos
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0 # Esta linea se utiliza para "inicializar", es una buena práctica

    if opcion == 1: # Sumar
        resultado = operando1 + operando2
        print(f"\nEl resultado de la suma es: {resultado}\n")

    elif opcion == 2: # Restar
        resultado = operando1 - operando2
        print(f"\nEl resultado de la resta es: {resultado}\n")

    elif opcion == 3: # Multiplicacion
        resultado = operando1 * operando2
        print(f"\nEl resultado de la multiplicacion es: {resultado}\n")

    elif opcion == 4: # Division
        resultado = operando1 / operando2
        print(f"\nEl resultado de la division es: {resultado}\n")

    elif opcion == 5: # Salir    
        print("\nSaliendo del programa de calculadora, hasta pronto\n")
        salir = True 
        
    else:
        print("\nOpcion invalda, selecciona otra opcion...\n")
    
    return salir

#Programa principal
if __name__ == "__main__":
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)

