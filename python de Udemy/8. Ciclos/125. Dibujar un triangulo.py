print("**** Dibujar triangulo simetrico ****")

numero_filas = int(input("Proporciona l numero de filas: "))

# Iterar sobre cada fila del trianguo
for fila in range(1, numero_filas + 1):
    espacios_blanco = " " * (numero_filas - fila)
    asteriscos = "*" * (2 * fila - 1)
    print(f"{espacios_blanco}{asteriscos}")
