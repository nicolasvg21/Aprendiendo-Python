print("**** Programa de listas con diccionario ***")    

print("\n---------Primera forma-------") # Abro con corchetes diciendo que es una LISTA DE DICCIONARIOS
personas = [
    {
        "nombre": "Regina",
        "apellido": "Flores",
        "edad": "21"       
    },
    {
        "nombre": "Alejandro",
        "apellido": "Reyes",
        "edad": "32"    
    }
]

print(personas)

print("\nContactos de la agenda")
for detalles in personas:
    print(f"""
    Nombre: {detalles['nombre']}
    Apellido: {detalles['apellido']}
    Edad: {detalles['edad']}""")

print("\n-----------Segunda forma---------------") # Se abre con llaves diciendo que es un DICCIONARIO DE DICCIONARIOS

personas = {
    "0": {
        "nombre": "Regina",
        "apellido": "Flores",
        "edad": "21"       
    },
    "1": {
        "nombre": "Alejandro",
        "apellido": "Reyes",
        "edad": "32"    
    }
}

print(personas)

print("\nContactos de la agenda")
for indice, detalles in personas.items():
    print(f"""Indice: {indice}
    Nombre: {detalles['nombre']}
    Apellido: {detalles['apellido']}
    Edad: {detalles['edad']}""")

print()
print("*** Así lo hace el profe ***") #-----------------------------------

personas =[
    {
        "nombre": "Regina",
        "apellido": "Flores",
        "edad": "21"
    },
    {
        "nombre": "Alejandro",
        "apellido": "Reyes",
        "edad": "32"
    }
]

print(personas)

# Acceder a un diccionario desde una lista
print(f"""\nDetalle del primer elemento de la lista
    Nombre: {personas[0].get("nombre")}
    Apellido: {personas[0]['apellido']}
    Edad: {personas[0]["edad"]}
""")

# Recorrer los elementos de la lista
for contador, persona in enumerate(personas):
    print(f"{contador} - Persona: {persona}")
    # print(f"Detalle: Nombre: {persona["nombre"]}, Apellido {persona['apellido']}, Edad: {persona["edad"]}")