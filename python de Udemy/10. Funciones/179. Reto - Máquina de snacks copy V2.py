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

def buscar_snack_por_id(id_buscar):
    for snack in inventarios:
        if snack.get("Id") == id_buscar:
            return snack
    # Si llemaos al final y no se encontró el snack regresa None
    return None

compras = []

def comprar_snack():
    print("\n--- Buscar por Id ---")
    id_snack = int(input("Qué snacks quieres comprar (Id): "))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        compras.append(snack_encontrado)
        print(f"Snack agregado: {snack_encontrado}")
    else:
        print(f"Snack NO encntrado con el id: {id_snack}")
           

def mostrar_ticket():
    if not compras:  # Si la lista está vacía
        print("No hay artículos agregados.")
        return
    
    total = 0
    print(f"\n--- Ticket de venta ---")
    for contador, snacks in enumerate(compras):
        print(f"{contador+1} - {snacks.get("Id")} -> {snacks.get("Nombre")} - ${snacks.get("Precio")}")
        total += snacks.get("Precio") # sumar unicamente los valores de precio
    print(f"\n{'='*40}")
    print(f"TOTAL PRODUCTOS: {len(compras)}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print(f"{'='*40}")

if __name__ == "__main__":
    while True:
        print("""\n--- Menú ---
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

        