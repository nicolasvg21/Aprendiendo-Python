print("*** Regresar una tupla de vlaores desde una funcion ***")

# Definicion de la función

def personas_mayusculas(nombre, apellido, edad):
    print(f"Esta funcion regreas varios valores (tupla)")
    return (nombre.upper(), apellido.upper(), edad) # python idetifica con las "," que es una tupla o tambien podrias ser mas específico y lo coloco entre paréntesis "()"

# Programa princiapl
nombre, apellido, edad =personas_mayusculas("Sandra", "Jimenez", 42) # Se está realizando un empaquetamiento de una tupla
print(f"Resultado personas: nombre: {nombre}, apellido:{apellido}, edad: {42}")







