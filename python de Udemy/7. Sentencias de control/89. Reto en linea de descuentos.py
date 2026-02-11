"""
Docstring for python de Udemy.7. Sentencias de control.89. Reto en linea de descuentos

Tienda en linea

Crear un sistema que ofrezca descuentos dependiendo del monto de la compra, o si es miembro de la tienda.

Se deben revisar las siguientes codnciiones:

1) Si ha comprado mas de $1.000 y es miembro -> descuento del 10%
2) Si solo es miembro de la tienda -> Descuento del 5%
3) Si no es mimebro ni campró mas de $1.000 -> Descuento de 0%
"""

print("*** SISTEMA DE DESCUENTOS ***")

monto = int(input("Cual es el monto de su compra?: "))
miembro = str(input("Eres miembro de la tienda (si/no)?: ").strip().lower())

monto10 = monto * 0.9
monto5 = monto * 0.95
monto15 = monto * 0.85

if monto >= 1000:
    print(f"\nperfecto, tu monto fue de {monto}, significa que puedes tener el descuento de 10%")
    
    if miembro == "si":
        print(f"\nTu respuesta fue {miembro}, significa que se te agrega otro 5% de descuento")
        print(f"""
El monto de la compra fue: ${monto}
El descuento fue del 15%
El precio a pagar es de: ${monto15}""")

    else:
        print(f"\ntu respuesta fue {miembro}, lo sentimos mucho pero no podemos darte el descuento adicional del 5%")
        print(f"""
El monto de la compra fue: ${monto}
El descuento fue del 10%
El precio a pagar es de: ${monto10}""")

elif miembro == "si":
    print(f"\nNo te podemos dar el descuento del 10% pero como tu respuesta fue ${miembro}, significa que tienes un descuento del 5%")
    print(f"""
El monto de la compra fue: ${monto}
El descuento fue del 5%
El precio a pagar es de: ${monto5}""")

else:
    print(f"\nlo siento pero no te podemos dar descuento y tu valor a pagar es de ${monto}")
print()

print("----------- así lo hace mi profe de udemy Ubaldo -------")
print()
print("*** SISTEMA TIENDA EN LINEA CON DESCUENTOS ***")
#condiciones
MONTO_COMPRA_DESC = 1000

monto_compra = float(input("Cual fue el monto de tu compra?: "))
es_miembro = input("Eres miembro de la tienda (Si/No)?: ")

descuento = 0
#verificar cada caso, con lso datos proporcionados 
if monto_compra >= MONTO_COMPRA_DESC and es_miembro.strip().lower() == "si":
    descuento = 0.1 # Descuento del 10%
elif es_miembro.strip().lower() == "si":
    descuento = 0.05 # Descuento del 5%
elif monto_compra >= MONTO_COMPRA_DESC:
    descuento = 0.03 # Descuento del 3%
else:
    descuento = 0 

# Hacemos los calculos respectivos para obtener el monto final
if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f"\nFelicidades, has obtenido un descuento del {descuento * 100:.0f}%")
    print(f"Monto de la compra: {monto_compra:.2}")
    print(f"Monto del descuento: {monto_descuento:.2f}")
    print(f"Monto final de la compra con descuento: ${monto_final:.2f}")
else:
    print("\nNo obtubviste ningun tipo de descuento")
    print("Te invitamos a hacerte iembro de la tienda")
    print(f"Monto final de la compr: {monto_compra:.2f}")
