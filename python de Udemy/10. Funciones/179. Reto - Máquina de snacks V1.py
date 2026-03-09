"""
Máquina de snacks

Crea un programa deonde podras compra snacks de una lista inicial

Cada snack tiene su id, nombre y precio

Para comprar un snack se bebe indicar el id del snack a comprar y se agregará un lista de productos comprados

Ademas se debe mostrar el ticket de venta final con el total de productos y el total de la venta
"""
print("*** Reto Máquina de snacks ***")

# Mostramos el inventario de snacks
inventarios = [
    {"Id": 1, "Nombre": "Papas", "Precio": 30},
    {"Id": 2, "Nombre": "Refresco", "Precio": 50},
    {"Id": 3, "Nombre": "Sandwich", "Precio": 120}
]

# Definir una funcion para el invnetario
def mostrar_inventario():
    print("\n--- Inventario de snacks ---")
    for contador, snacks in enumerate(inventarios):
        print(f"{contador} - Id: {snacks.get("Id")} -> {snacks.get("nombre")} - ${snacks.get("Precio")}")

compras = []



def comprar_snack():
    print("\n--- Buscar por Id ---")
    id_buscar = int(input("Qué snacks quieres comprar (Id): "))
    
    for snacks in inventarios:
        if snacks.get("Id") == id_buscar:
            id = snacks.get("Id")
            nombre = snacks.get("Nombre")
            precio = snacks.get("Precio")

            # Creamos el nuevo producto para la compra
            agregar_snack = {"Id": id, "Nombre": nombre, "Precio": precio}

            # Agregamos el nuevo producto a la lista de comrpra
            compras.append(agregar_snack)
            print(f"El producto:")
            for inventario in compras:
                print(inventario)
                print("fue agregado la lista de compras satisfactoriamente!")
            return
    print("El Id no fue encontrado")
            

def mostrar_ticket():
    if not compras:  # Si la lista está vacía
        print("No hay artículos agregados.")
        return
    
    total = 0
    print(f"\n--- Ticket de venta ---")
    for contador, snacks in enumerate(compras):
        print(f"{contador+1} - Id: {snacks.get("Id")} -> {snacks.get("Nombre")} - ${snacks.get("Precio")}")
        total += snacks.get("Precio") # sumar unicamente los valores de precio
    print(f"\n{'='*40}")
    print(f"TOTAL PRODUCTOS: {len(compras)}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print(f"{'='*40}")



if __name__ == "__main__":
    while True:
        print(f"""\n--- Menú ---
        1. Mostrar snacks
        2. Comprar snacks
        3. Mostrar ticket
        4. Salir""")

        opcion = int(input("\nEscoge una opcion: "))
        if opcion == 1:
            mostrar_inventario()

        elif opcion == 2:
            comprar_snack()

        elif opcion == 3:
            mostrar_ticket()
        
        elif opcion == 4:
            print("Regresa pronto!")
            break
        else:
            print("Intentalo de nuevo, tu numero no está en el rango de 1-4")

        