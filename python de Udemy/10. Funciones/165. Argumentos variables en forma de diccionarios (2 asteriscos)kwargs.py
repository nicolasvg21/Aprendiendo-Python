# *args - argumens - tupla
# **kwargs - keywords arguments(key,value) como un diccionario
print("*** Argumentos variables en forma de diccionario ***")

def superheroe_superpoderes(nombre, apellido, *args, **kwargs):
    print(f"Superheroe: {nombre} {apellido}- {args} - Mas informacion: {kwargs}")

# Llamamaos la funcion
superheroe_superpoderes("Spidereman", "Parker", "Instinto aracnido", edad=17, empresa="Marvel")

superheroe_superpoderes("Ironman", "stark", "Armadura", "Millonario", edad=45)

superheroe_superpoderes("Mi vecino", "padilla", edad="es un sapo hpta")