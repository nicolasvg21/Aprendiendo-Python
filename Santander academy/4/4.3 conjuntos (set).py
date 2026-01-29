print("4.3. CONJUNTOS(SET)")
print("Un conjunto es una estructura de datos mutable u no ordenada que permite almacenar una coleccion de elementos unicos. Los conjuntos se encierran entre llaves {} o se crean utilizando la funcion set()")
print("")

print("CREACION Y OPERACIONES BASICAS")
print("Para crear un conjunto, puedes utilizar llaves o la funcion set().")
print("")

frutas = {"manzana", "banana", "naranaja"}
numeros = set([1, 2, 3, 4, 5])

print("Los conjuntos admiten operaciones matematicas de conjuntos, como:")
print("")

print("Imagina que los conjuntos son conjunto1 = {1, 2, 3} y conjunto2 = {3, 4, 5}")
print("")

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

print("la union (|)")
union = conjunto1 | conjunto2
print(union)
print("")

print("la interseccion (&)")
interseccion = conjunto1 & conjunto2
print(interseccion)
print("")

print("la diferencia (-)")
diferencia = conjunto1 - conjunto2
print(diferencia)
print("la razón por la que el resultado es {1, 2} es que estos son los elementos que están en conjunto1 pero no en conjunto2 y el numero 3 si aparece en ambos conjuntos pero lo que sucede es que se descarta ya que la diferencia solo toma los elementos unicos de conjunto1 que no estan en conjunto2.")
print("")

print("la diferencia simetrica (^)")
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)
print("")

print("METODOS DE CONJUNTOS")