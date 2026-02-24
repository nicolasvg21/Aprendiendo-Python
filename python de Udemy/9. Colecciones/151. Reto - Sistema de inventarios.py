"""
Gestion de inventario

Crea un programa para gestionar el inventario de un almacen.

Para ello se debe utilizar una lista de python par aamntener un registro de los productos disponibles en el almacén.

Y para almacenar el detalle del prducto se debe utilzr un diccionario, con el id, nombre, precio y cantidad disponible del producto.
"""
print("**** Sistema de inventarios ")

inventario = []
numero_productos = int(input("Cuantos productos deseas agregar al invnetario? "))

for indice in range(numero_productos):
    print(f"Proporciona los valores del producto {indice+1}")
    nombre = input("Nombre: ")
    precio = float(input("Precio: $"))
    cantidad = int(input("Cantidad: "))
    # Creamos el diccionario con el detalle del producto
    producto = {"id":indice+1, "nombre":nombre, "precio": precio, "cantidad": cantidad}
    # Agregamos el nuevo producto al inventario
    inventario.append(producto)

# Mostramos el inventario inicial
print(f"\nInventario inicial: {inventario}")

#buscar un producto por id
id_buscar = int(input("Ingresa el ID del producto a buscar"))
if 1 <= id_buscar <= numero_productos:
    print(f"""\nDetalles del producto segun el id:
          ID: {inventario[id_buscar]["id"]}
          Nombre: {inventario[id_buscar]["nombre"]}.
          Precio: ${inventario.get(id_buscar).get("precio"):.2f}
          Cantidad: {inventario.get(id_buscar).get("cantidad")}""")
else:
    print("Vea pedaso de basura si le sale este mensaje es porque ud es un idiota y no sabe seguir indicaciones, como va a poner un id que no aparece en la mlp lista que le coloqué en la linea de codigo 26")

print("\nInventario detallado actualizado")
for detalles in inventario:
    print(f"""ID: {detalles["id"]}
    Nombre: {detalles['nombre']}
    Precio: ${detalles.get('precio'):.2f}
    Cantidad: {detalles.get('cantidad')}""")







