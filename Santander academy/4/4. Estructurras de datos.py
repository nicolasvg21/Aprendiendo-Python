print ("LISTAS")
print ("CREACIÓN Y ACCESO")
print ("Para crear una lista simplemetne encierra los elementso entre corchetes:")
frutas = ["Manzana", "banana", "naranja"]
print ("")

print(frutas[0]) 
print(frutas[1])
print(frutas[2])
print ("")

print ("tambien puedes nombrar objetos de la lista de abajo hacia arriba solo con colocar un negrativo (-) antes del numero, empezando con el -1 para el ultimo dato, -2 para el penultimo dato y asi sucesivamente")
print ("")

print(frutas[-1])
print(frutas[-2])
print(frutas[-3])
print ("Metodos de la listas")
print ("1. append(elemento):         Agrega un elemento al final de la lista.")
print ("2. insert(indice, elemento): Inserta un elemento en la posicion especifica de la lista.")
print ("3. remove(elemento):         Elimina la primera aparcion de un elemento en la lista.")
print ("4. pop(indice):              Elimina y devuelve el elemento de una poscion especifica de la lista.")
print ("5. sort():                   Ordena los elemento de la lsita en orden ascendente.")
print ("6. reverse():                Invierte el orden de los elemento en la lsita.")
frutas = ["manzana","banana", "naranja"]
print("")

frutas.append("pera")
print (frutas)
print ("")

frutas.insert(1, "uva")
print(frutas)
print("")

frutas.remove("banana")
print (frutas)
print ("")

fruta_eliminada = frutas.pop(2)
print(frutas)
print (fruta_eliminada)
print ("")

frutas.sort()
print(frutas)
print ("")

frutas.reverse()
print(frutas)

print("LISTA DE COMPRESIÓN")
print("Last lsitas de comprensión son una forma concisa de crear nuevas listas basadas en una secuencia existente. Permiten filtrar y transformar los elementos de ua lista en una sola linea de codigo.")
print ("")

print ("nueva_lista = [expresion for elemento in secuancia if condicon]")
print ("")

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x %2 == 0]
print(cuadrados)
print ("")

print("En este ejemplo se crea una nueva lsita llamda, cuadrados, que contiene los cuadradso de los elementos apres de la lista, la expersion x ** 2 eleva cada elemento al cuadrado, y la condicion if x % 2 == 0 filtra solo los nuemeros pares.")