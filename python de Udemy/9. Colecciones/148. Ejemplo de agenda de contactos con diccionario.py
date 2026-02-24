print("*** Agenda de contactos ****")

agenda = {
    "Carlos": {
        "telefono" : "3156577992",
        "email": "carlos@mail.com",
        "direccion": "tu puta madre"
    },
    "Maria": {
        "telefono": "3163960079",
        "email": "maria@mail.com",
        "direccion": "tu reputamadre"
    },
    "Pedro": {
        "telefono": "3108601484",
        "email": "pedro@mail.com",
        "direccion": "me la pelas"
    }
}

print(agenda)

# Acceder a la informacion de un contacto específico

print(f"""Informacion del contacto de María:
      Telefono: {agenda['Maria']['telefono']},
      Email: {agenda.get("Maria").get("email")},
      Direccion: {agenda.get("Maria").get("direccion")}""")

# Agregar un nuevo contacto
agenda["Ana"] = {
    "teledono": "3154986678",
    "email": "ana@mail.com",
    "direccion": "maldita sabandija"
}

print(agenda)

# Eliminar un contacto existente
agenda.pop("Pedro")
# del agenda["Pedro"]
print(agenda)

# Mostramos los contactos de la agenda
print("\nContactos en la agenda")
for nombre, detalles in agenda.items():
    print(f"""Nombre: {nombre}
    Telefono: {detalles.get("telefono")},
    Email: {detalles.get("email")},
    Direccion: {detalles.get("direccion")}
""")