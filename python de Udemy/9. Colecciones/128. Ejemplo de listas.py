print("*** Manejo de listas*** ")

mi_lista = [1, 2, 3, 4, 5]
print(f"\n{mi_lista} - > Lista original")


#Largo de una lsita
print(f"\nLargo de una lsita: {len(mi_lista)}")

# Acceder a los elementos de la lsita por indice
print(f"\nAccedemso al valor del indice 4: {mi_lista[4]}")
print(f"\nAccedemos al ultimo valor del indice de la lista: {mi_lista[-1]}")

#modificar los elementos de una lsita
mi_lista[1] = 10
print(f"\nModificamos el valor del indice 1: {mi_lista}")

# Agregar un nuevo elemento al final de la lsita
mi_lista.append(6)
print(f"\n{mi_lista} -> Se agregó el elemento 6")

# Añadir un nuevo elemento en unindice específico
mi_lista.insert(2, 15)
print(f"\n{mi_lista} -> Se añadió el valor de 15 en el indice 2")

# Eliminar elementos de una lista
# Usando el método remove para eliminar un "VALOR"
mi_lista.remove(5)
print(f"\n{mi_lista} -> Se removió el valor de 5")

# Removemos por "INDICE" con el metodo pop
mi_lista.pop(1) # Remueve el elemento del indice 1 de la lista
print(f"\n{mi_lista} -> Se eleminó el INDICE 1")

#Eliminar un "INDICE" usando la palabra del
del mi_lista[2]
print(f"\n{mi_lista} -> Se eliminó el indice 2 es decir el valor de 3")

# Obtener sublistas
sublita = mi_lista[1:3]  # Genere una sublisata del indice 1 al 2 (3 no se incluye)
print(f"\nSublista [1:3]: {sublita}")