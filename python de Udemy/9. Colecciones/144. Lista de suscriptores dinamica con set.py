"""
Lista de suscrpciones

Crea un programa para administrar una lista de suscriptores utilziando su email.

Supón que una persona se suscribe al boletein informativo utilizando su email.

A medida que la lista crecem hay que asegurarnos que no tengamos suscriptores duplicados.

Tambien deberemos poder agregar y eliminar suscriptores.
"""
print("*** Lista de suscriptores ***")

# Definimos el set incial
#suscriptores = {} # Aqui se define un diccionario vacio
suscriptores = set() # Definimos un set vacio

numero_suscriptores = int(input("Proporciona el numero d esuscriptres iniciales: "))
for _ in range(numero_suscriptores):
    suscriptores.add(input("Nuevo suscriptor (email): "))

print(f"\nLista de suscriptores inicial: {suscriptores}")

# Verifica si un nuevo suscriptores está en la lista
nuevo_suscriptor = input("Proporciona el nuevo suscriptor: ")
if nuevo_suscriptor in suscriptores:
    print(f"\nEl nuevo suscriptor ya está en la lista {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"\nEl nuevo suscriptor ya se ha agregado a la lista {nuevo_suscriptor}")
print(f"\nLista de suscriptores actualizada: {suscriptores}")

# Eliminamos un suscriptor
suscriptor_eliminar = input("Proporcioan el suscriptor a eliminar: ")
suscriptores.remove(suscriptor_eliminar)
print(f"\nEl susciptor {suscriptor_eliminar} ha sido elminado de la lista")
print(f"\nLista de suscriptores: {suscriptores}")

# Verificamos la cantidad total de suscriptores
print(f"\nCantidad total suscriptores: {len(suscriptores)}")

# Mostramos todos los suscriptores
print(f"\n---- Lista de suscripters ------")
for suscriptor in suscriptores:
    print(f"- {suscriptor}")