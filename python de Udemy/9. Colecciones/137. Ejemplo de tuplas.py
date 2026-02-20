print("*** Manejo de tuplas ***")

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
# No podemos modfiicar una tupla
# mi_tupla[0] = 10
# mi_tupla.append(0)

# Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento, end=" ")

# Crear una tupla para una coordenada x,y
coordenada = (3, 5)
# Accedemos a cada elemento de la tupla
print(f"\nCoordenada en el eje x: {coordenada[0]}")
print(f"Coordenada en el eje y: {coordenada[1]}")

# Crear una tupla unitaria
tupla_un_elemento = 10,
print(f"Tupla de un elemento: {tupla_un_elemento}")

# Tupla anidada
tupla_anidada = (1, (2,3), (4, 5))
print(f"Segundo elemento tupla anidada: {tupla_anidada[1]}")