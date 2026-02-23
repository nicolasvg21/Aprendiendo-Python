print("*** manejo de sets ***")

#Crear un conjunto
mi_set = {1, 2, 3, 4, 5, 4}
print(f"Mi set: {mi_set}")

# Agregar elementos al set
mi_set.add(6)
mi_set.add(7)
print(f"Mi set modificado: {mi_set}")

# Intentamos agregar un elemtno duplicado
mi_set.add(3)
print(f"Mi set modificado: {mi_set}")

# Eliminar un elemnto del conjunto
mi_set.remove(4)
print(f"Mi set modificado: {mi_set}")

# Iterar los elementos del set
for elemnto in mi_set:
    print(elemnto, end=" ")

# comprobar si existe un elemento en el set
print(f"\nExiste el valor de 4 en el set: {4 in mi_set}")
print(f"\nExiste el valor de 1 en el set: {1 in mi_set}")

# Obtener la longitud del set
print(f"Longitud del conjunto: {len(mi_set)}")
