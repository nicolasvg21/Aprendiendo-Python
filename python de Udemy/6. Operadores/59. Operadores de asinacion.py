#Operadores de asignacion

numero = 5
print(f"Valor de numero: {numero}")
numero = 10
print(f"\nValor de numero: {numero}")
cadena = "saludos desde python"
print(f"\nvalor de la cadena: {cadena}")

# Asignacion multple
x, y, z = 5, "hola", -9.15
print(f"\nx = {x}, y = {y}, z = {z}")

# Asignacion encadenada
a = b = c = 10
print(f"\nValor de a = {a}, valor de b = {b}, valor de c = {c}")

# Intercabio de valores de una varibale, sin utilizar variables temporales
x, y = 5, 10
print(f"\nValores iniciales de x = {x}, y = {y}")

#aplicando el concepto de asignacion multiple, intercambiamos valores
x, y = y, x
print(f"\nfInvertir los valores x = {x}, y = {y}")

# Recibir multilpes valores de entrada del usuario
nombre, apellido = input("\ningresar tu nombre y apellido separados por coma: ").split(",")

print(f"Nombre: {nombre}, apellido: {apellido}")