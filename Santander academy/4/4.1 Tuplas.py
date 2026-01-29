print("TUPLAS")
print("CREACION Y ACCESO")
print ("")

print("Para crear una tupla encierra los elementos entre paréntesis:")"
punto = (3, 4)

print("Para acceder a los elementos de una tupla, utiliza el indice del elemento entre corchetes, similar a las listas:")
print(punto[0])
print(punto[1])
print ("")

print("- A difrencia de las listas, las tuplas son inmutables, lo que significa que no se peuden modificar una vez creadas. No se pueden agregar, eliminar o cambiar elementos de una tupla exitente.")
print("- Las tuplas son utiles cuando necesitas almacenar una coleccion de elementos que nos se deben modficarse como coordenadas o datos de configuracion.")


print("METODOS DE TUPALAS")
print ("")
print("Aunque las tuplas son inmutables, Python proporciona variso metodos utiles para trabajar con ellas:")

mi_tupla = (1, 2, 3, 2, 4, 2)

print("count(elemnto): Devuelve el numero de veces que aparece un elemento en una tupla.")
print (mi_tupla.count(3))
print("")

print("index(elemento): devuelve el indice de la primera aparicion de un elemento en la tupla")
print("Opcionalmente, se puede especificar el inicio y fin de la busqueda")
print (mi_tupla.index(2))
print (mi_tupla.index(2, 2))
print (mi_tupla.index(2, 2, 4))
print("")

print("Len(tupla): aunque no es un metodo de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.")
#NO ENTENDÍ UNA MIERDA DE ESTOS MÉTODOS DE TUPLAS LA PLENA