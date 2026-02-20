print("*** Repeticion de un mensaje ***")

mensaje = input("Proporciona un mensaje a repetir: ")
numero_de_repeticiones = int(input("Proporciona el numero de repeticioes: "))

# Iterar osbre el rango de repeticiones:
for i in range(numero_de_repeticiones):
    print(f"{i+1} - {mensaje}")
print()
for _ in range(numero_de_repeticiones):
    print(mensaje)    

