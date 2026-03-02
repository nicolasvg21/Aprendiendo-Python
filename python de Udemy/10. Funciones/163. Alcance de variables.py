print("*** Alcance de variables ***")

# Variable global
contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0

    # Usar la variable global
    global contador_global
    contador_global += 1

    # Incrementar la variable local
    contador_local += 1

    # Imprimir ambos contadores
    print(f"Contador local {contador_local}")
    print(f"Contador global: {contador_global}\n")

# Llamamos varias veces
incrementar_contador()
incrementar_contador()
incrementar_contador()
# Al correr el programa se evidencia que la variable local se reescribe todo el tiempo dando el valor de 1, pero la variable local es diferente, se utiliza a lo largo de todo el programa por lo que no se destruye con cada llamada a la función

# Terminando el programa
print(f"Valor variable global: {contador_global}")