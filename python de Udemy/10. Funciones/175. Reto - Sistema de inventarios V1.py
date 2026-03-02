"""
Sistema de inventarios

Crear un sistema de invnetarios que tenga las siguientes opciones:

Mostras un menú:
    1: Mostrar inventario
    2: Agregar nuevo producto
    3. Buscar prodcuto por ID
    4. Salir

Detalle de un producto:
    ID
    Nombre
    precio
    Cantidad
"""

print("*** Sistema de inventario con funciones ***")

inventarios = [
    {
        "Id" : 0,
        "Nombre" : "Camisa",
        "Precio" : 25.99,
        "Cantidad" : 50,
    },
    {
        "Id" : 1,
        "Nombre" : "Pantalones",
        "Precio" : 39.99,
        "Cantidad" : 30
    },
    {
        "Id" : 2,
        "Nombre" : "Zapatos",
        "Precio" : 49.99,
        "Cantidad" : 20
    }
]

menu = True
while menu:
    print(f"""\nMenú:
    1. Mostrar inventario
    2. Agregar nuevo producto al inventario
    3. Buscar producto por id
    4. Salir""")
    opcion = int(input("\nElige una opcion del 1-4: "))
    if 1 <= opcion <= 4:
        if opcion == 1:
            print(f"\nEl inventario es:")
            for inventario in inventarios:
                print(inventario)

        elif opcion == 2:
            print(f"\nAgrega los siguientes valores: ")
            id = int(input("El id siguiente que corresponde: "))
            nombre = input("Nombre del producto: ")
            precio = float(input("El precio del producto: $"))
            cantidad = int(input("Cuantas unidades hay del producto:"))
            
            # Creamos el diccionario con el detalle del producto:
            producto = {"Id":id, "Nombre":nombre, "Precio":precio, "Cantidad": cantidad}
            # Agregamos el nuevo prodcuto al inventario
            inventarios.append(producto)
            print("El producto fue agregado satisfactoriamente!")

        elif opcion == 3:
            id_buscar = int(input("\nIngresa el ID del producto a buscar: "))
            tamanio_inventario = len(inventarios)
            print(f"Este es el tamaño del invnetario {tamanio_inventario}")

            if 0 <= id_buscar <= tamanio_inventario-1:
                print(f"""\nDetalles del producto con id {id_buscar}:
        ID: {inventarios[id_buscar].get("Id")}
        Nombre: {inventarios[id_buscar].get("Nombre")}
        Precio: ${inventarios[id_buscar].get("Precio"):.2f}
        Cantidad: {inventarios[id_buscar].get("Cantidad")}""")
                
            else:
                print(f"El id {id_buscar} no fue encontrado")
        
        else:
            print("Lograste salir con exito, vuelve pronto!")
            menu = False
    else:
        print("Ud es un bobo hpta, tiene que colocar un numero del 1 al 4, intente otra vez idiota")
