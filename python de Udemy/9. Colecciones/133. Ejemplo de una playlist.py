print("**** Playlist de canciones ****")

# Creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input("\nCuantas canciones deseas agregar: "))

# Iteramos cada elemento de  la lsita para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f"Proporciona la cancion {indice + 1}: ")
    lista_reproduccion.append(cancion)


# Ordenar la lista en orden alfabético .sort()
# lista_reproduccion.sort()
# Ordenar la lista en orden alfabético pero al reves .sort(reverse=True)
# lista_reproduccion.sort(reverse=True)

# Mostrar la lista iterando sus elementos
print("\nIteramos la playlist")
for cancion in lista_reproduccion:
    print(f"{cancion}")