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

#inventario de nuestro almacen
inventario = [
    {"Id" : 1, "Nombre" : "Camisa", "Precio" : 25.99, "Cantidad" : 50},
    {"Id" : 2, "Nombre" : "Pantalones", "Precio" : 39.99, "Cantidad" : 30},
    {"Id" : 3, "Nombre" : "Zapatos", "Precio" : 49.99, "Cantidad" : 20}
]

# Definir una funcion para el inventario
def mostrar_inventario():
    print("\n--- Inventario del almacen ---")
    for contador, producto in enumerate(inventario):
        print(f"{contador} - Id: {producto.get("Id")}, Nombre: {producto.get("Nombre")}, Precio: ${producto.get("Precio")}, Cantidad: {producto.get("Cantidad")}")

def agregar_producto():
    #pass
    print(f"\nAgrega los siguientes valores: ")
    id = int(input("Id: "))
    nombre = input("Nombre: ")
    precio = float(input("Precio: $"))
    cantidad = int(input("Cantidad: "))

    # Con esta nueva linea de código ahora puede validad si existe el id y decirme ey bro no pudes agregarlo porque ya existe perro hpta
    for prod in inventario:                         
        if prod.get("Id") == id:
            print("¡ERROR! Ese id ya existe.")
            return # Sale sin guardar
    
    # Creamos el diccionario con el detalle del producto:
    nuevo_producto = {"Id":id, "Nombre":nombre, "Precio":precio, "Cantidad": cantidad}
    # Agregamos el nuevo prodcuto al inventario
    inventario.append(nuevo_producto)
    print("El producto fue agregado satisfactoriamente!")
    
def buscar_producto_id():
    print("\n--- Buscar producto por Id ---")
    id_buscar = int(input("\nIngresa el ID del producto a buscar: "))
    for producto in inventario:
        if producto.get("Id") == id_buscar:
            print(f"""\nDetalles del producto encontrado:
        ID: {producto.get("Id")} 
        Nombre: {producto.get("Nombre")} 
        Precio: ${producto.get("Precio"):.2f} 
        Cantidad: {producto.get("Cantidad")}""")
            return
    print("Producto no encontrado")

# Programa principal
if __name__ == "__main__":
    while True:
        print(f"""\n--- Menú---
        1. Mostrar inventario
        2. Agregar nuevo producto al inventario
        3. Buscar producto por id
        4. Salir""")
        opcion = int(input("\nElige una opcion del 1-4: "))

        #Revisamos las opciones del menú
        
        if opcion == 1: # Mostrar el inventario
            print(f"\nEl inventario es:")
            mostrar_inventario()

        elif opcion == 2: # Agregar un nuevo prodcuto
            agregar_producto()
            
        elif opcion == 3:
            buscar_producto_id()
                    
        elif opcion == 4:
            print("Lograste salir con exito, vuelve pronto!")
            break
        
        else:
            print("Ud es un bobo hpta, tiene que colocar un numero del 1 al 4, intente otra vez idiota")