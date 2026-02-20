print("*** break y continue ****")

# Ejemplo con break
print("Palabra break")
for numero in range(1, 10):
    if numero % 2 == 0: # al usar el modulo % de 2 significa el que numero que se divide es par
        print(numero)
        break # salimos del cilo inmediantemente
print()
# Ejemplo con continue
print("Palabra continue")
for numero in range(1, 10):
    if numero % 2 == 1: # numero impar
        continue
    print(numero) # Solo numero pares