print("*** Suma con argumentos variables ***")

# Funcion sumar que acepta argumentso variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Llamamos a la funcion sumar
sumar(1, 2, 3, 4, 5)
resultado = sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Resultado de la suma: {resultado}")