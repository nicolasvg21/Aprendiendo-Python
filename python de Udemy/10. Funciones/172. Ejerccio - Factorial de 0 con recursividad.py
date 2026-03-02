print("*** Factorial del numero 5 ***")

# Definimos la funcon factorial recursiva
def factorial_recursiva(numero):
    # Caso base, factorial 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f"Reusltado factorial parcial {numero} es: 1")
        return 1
    
    else: # Caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f"Resultado factorial parcial {numero} es: {factorial_parcial}")
        return factorial_parcial

numero = 4
resultado = factorial_recursiva(numero)
print(f"\nEl factorial de {numero} es: {resultado}")