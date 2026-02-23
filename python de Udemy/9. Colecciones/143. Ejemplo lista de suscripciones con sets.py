"""
Lista de suscrpciones

Crea un programa para administrar una lista de suscriptores utilziando su email.

Supón que una persona se suscribe al boletein informativo utilizando su email.

A medida que la lista crecem hay que asegurarnos que no tengamos suscriptores duplicados.

Tambien deberemos poder agregar y eliminar suscriptores.
"""
print("*** Lista de suscriptores ***")

suscriptores = {"luisa@mail.com", "marcos@mail.com", "elena@mail.com"}
print(f"\nLista de suscriptores inicial: {suscriptores}")

# Verifica si un nuevo suscriptores está en la lista
nuevo_suscriptor = "karla@mail.com"
if nuevo_suscriptor in suscriptores:
    print(f"\nEl nuevo suscriptor ya está en la lista {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"\nEl nuevo suscriptor ya se ha agregado a la lista {nuevo_suscriptor}")
print(f"\nLista de suscriptores actualizada: {suscriptores}")

# Eliminamos un suscriptor
suscriptor_eliminar = "elena@mail.com"
suscriptores.remove(suscriptor_eliminar)
print(f"\nEl susciptor {suscriptor_eliminar} ha sido elminado de la lista")
print(f"\nLista de suscriptores actualziada: {suscriptores}")

# Verificamos la cantidad total de suscriptores
print(f"\nCantidad total suscriptores: {len(suscriptores)}")

# Mostramos todos los suscriptores
print(f"\n---- Lista de suscripters ------")
for suscriptor in suscriptores:
    print(f"- {suscriptor}")

