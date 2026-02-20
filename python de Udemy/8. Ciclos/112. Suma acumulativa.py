print("*** suma acummulativa ***")

#sumar los 5 primeros numeros
MAXIMO = 4
numero = 1
acumulador_suma = 0

# Empezamos a iterar
while numero <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f"(acumulador_suma + numero) -> {acumulador_suma} + {numero}")

    acumulador_suma += numero
    numero += 1 # Lo mismo que decir numero = numero + 1

    # Imprimir el resultado de la suma parcial
    print(f"Suma parcial acumulada: {acumulador_suma}\n")


print(f"\nResultado de la suma acumulada: {acumulador_suma}")