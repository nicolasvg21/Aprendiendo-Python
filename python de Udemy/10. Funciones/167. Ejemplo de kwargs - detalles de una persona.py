print("*** Imprmir detalles de una persona usando kwargs ***")

# Funcion que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print("\nValores recibidos:\n")
    for llave, valor in kwargs.items():
        print(f"{llave}:{valor}")

# Llamamos a la funcion
imprimir_detalle_persona(nombre="karla", edad=30, ciudad="Mexico")
imprimir_detalle_persona(nombre="Carlos", edad=28, ciudad="Guadalajara", puesto="Gerente")