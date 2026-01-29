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
print("Los conjuntos en python tienen varios métodos incorporados para maipular y acceder a los elemento. Algunos métoos comunes son:")
print("")

Frutas = {"manzana", "banana", "naranja"}

print("- add(elemento: agrega un elemento al conjunto.")
frutas.add("pera")
print(frutas)
print("")

print("- remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.")
frutas.remove("banana")
print(frutas)
print("")

print("- discard(elemento: elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.")
frutas.discard("uva")
print(frutas)
print("")

print("- clear(): elimina todos los elementos del conjunto.")
frutas.clear()
print(frutas)
print("")

print("Las estructuras de datos de python nos brindan una gran flexibilidad y potencia para almacenar y manipular datos en nuestros programas. Las listas son utiles para colecciones ordenadas y mutables, las tuplas para colecciones ordenadas e inmutables, los diccionarios para almacenar pares clave-valor y los conjuntos para colecciones no ordenadas de elementos unicos.")
print("")
