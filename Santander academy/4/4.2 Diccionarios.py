print("DICCIONARIOS")
# Un diccionario es un aestructura de datos mutable y no odenada que permite almacenar pares de clave-valor. Cada elemento en un diccionario consiste en un aclae unica y su valor correspondiente. Los diccionarios se encierran en llames {}, y los pares clave-valor se separan por comas.
print()

print("CREACION Y ACCESO")
# Para crear un diccionario, utiliza llaves y separa las calves y alores con dos puntos.
print()

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# puedes acceder a los vlaores de un diccionario, utiliza la clave correspondiente entre corchetes:
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])

# También puedes utilizar el método get() para obtener el valor de una clave. Si a clave no existe, devuelve un valor predeterminado (por defecto, None).
print()
 
print ("METODOS DE DICCIONARIOS")
# Los diccionarios en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:
print()

# keys(): devuelve una vista de todas las claves del diccionario.
print(persona.keys())
print()

# values(): devuelve una vista de todos los valores del diccionario
print(persona.values())
print()

# items(): devuelve una vista de todos los pares clave-valor del diccionario
print(persona.items())
print()

# update(otro_diccionario): actualiza el diccionarios con los pares clave-valor de otro diccionario
persona.update({"profesion":"Ingeniero"})
print(persona)
print()
