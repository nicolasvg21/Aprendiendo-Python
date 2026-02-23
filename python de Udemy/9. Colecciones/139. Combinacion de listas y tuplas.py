print("**** COMBINACION DE LISTAS CON TUPLAS ****")

# definir una lista que alcancemos tuplas de productos
productos = [
    ("P001", "Camiseta", 20.00),
    ("P002", "Jeans", 30.00),
    ("P003", "Sudadera", 40.00),
]

# Imprimir la informacion de cada producto y ademas calculamos el precio total
precio_total = 0

print("\nInformacion de los productos: ")
for producto in productos:
    # print(producto)
    id, descripcion, precio = producto # unpacking
    print(f"Producto: id = {id}, descripcion = {descripcion}, precio = {precio} ")
    precio_total += precio # producto[2]
print(f"\nPrecio total de los prodcutos: ${precio_total}")