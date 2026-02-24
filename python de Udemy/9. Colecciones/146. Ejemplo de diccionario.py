print("*** Diccionarios en python ***")

# Creamos un dict de persona con clave y valor
persona = {
    "nombre": "Sergio",
    "edad": 30,
    "ciudad": "Mexico"
}
print(f"\nDiccionario de persona: {persona}")

# Acceder a los elementos del diccionario
print(f"Nombre: {persona["nombre"]}")
print(f"Edad: {persona.get("edad")}")
print(f"Ciudad: {persona['ciudad']}")

#Modificar un valor del diccionario
persona["edad"] = 35
print(f"\nDiccionario de persona: {persona}")

# Agregar un nuevo elemento
persona["profesion"] = "Ingeniero"
print(f"\nDiccionario de persona: {persona}")

# Eliminar un elemento del diccionario
del persona["ciudad"]
print(f"\nDiccionario de persona: {persona}")

persona.pop("profesion")
print(f"\nDiccionario de persona: {persona}")

# Iterar los elementos de un dict (llave, valor
for llave, valor in persona.items():
    print(f"\nLlave: {llave}, Valor: {valor}")

# Obterner los valores
print("\nValores del diccionario: ")
for valor in persona.values():
    print(f"- Valor: {valor}")

# Obtener las llaves
print(f"Impresion de las llaves del diccionario: ")
for llave in persona.keys():
    print(f"- Llave: {llave}")

print(persona.items())
print(persona.keys())
print(persona.values())