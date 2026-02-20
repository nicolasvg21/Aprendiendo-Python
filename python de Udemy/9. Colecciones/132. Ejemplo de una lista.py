"""
Lista de reproduccion 

Crea un programa para administrar una lsita de conciones.

Debes solicitar al usario cuantas canciones desea agregar a la lista y posteriormente ir solicitando cada cancion que desea agregar a la lista.

Finalmente debe desplegar la lsita de canciones en orden alfabético.
"""

print("**** Playlist de canciones ****")

# Creamos la lista vacia
lista_reproduccion = []

# Empezamos a agregar canciones
lista_reproduccion.append("Hotel california - Eagles")
lista_reproduccion.append("Staying alive - bee gees")
lista_reproduccion.append("Dream on - Aerosmith")

# Ordenar la lista en orden alfabético. sort
lista_reproduccion.sort()
# Mostrar lista  de canciones 
print(f"\nLista de reproduccion en orden alfabético:")
print(lista_reproduccion)

# Ordenar la lista en orden alfabético pero al reves. sort
lista_reproduccion.sort(reverse=True)
# Mostrar lista  de canciones 
print(f"\nLista de reproduccion en orden alfabético inverso:")
print(lista_reproduccion)
print()

# Mostrar la lista iterando sus elementos
print("\nIteramos la playlist")
for cancion in lista_reproduccion:
    print(f"- {cancion}")