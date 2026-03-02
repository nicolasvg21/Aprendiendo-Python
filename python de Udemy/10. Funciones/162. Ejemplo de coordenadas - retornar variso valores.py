print("*** Obtener coordenadas x, y, z ***")

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return (x, y, z)

# Llamar la funcion
resultado = obtener_coordenadas() # No se aplica el concepto de empaquetamiento, solo es una tupla completa
print(resultado)

# unpacking o empaquetamiento de la tupla
x1, y1, z1 = resultado
print(f"Coordenada x = {x1}, Coordenada y = {y1}, Coordeanda z = {z1}")

suma = x1 + y1 + z1
print(suma)