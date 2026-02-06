"""
Docstring for python de Udemy.6. Operadores.72. Ejemplo ticket de venta

GENERACON DE TICKET DE VENTA

Supongamos qu ecompramos varios articulos en el supermercado y queremos obtener el ticket de venta total incluyendo impuestos.

El sistema solicitará el precio de cada preoducto a comprar y el usuario deberá indicar su precio (valor de tipo con punto decimal)

El sistema debe realizar la suma de cad producto, calcular el impuesto y finalmente imprimir el total de la compra
"""

print("**** GENERADOR DE TICKET DE VENTA ****")
print()
precio_leche = float(input("precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("precio precio_lechuga: "))
precio_platanos = float(input("precio platanos: "))
descuento_porcentaje = int(input("Aplicar algun descuento (%)? "))

#calculo de subtotoal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

#Aplicar el descuento
descuento =subtotal * (descuento_porcentaje/100)

# Subtutola con decuento
subtotal_con_descuento = subtotal - descuento

# Calculo con impuestos (16%)
impuesto = subtotal_con_descuento * 0.16

#caulculo total de la compra (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f"""
Subtotal: ${subtotal:.2f}
Descuento: del {descuento_porcentaje}% equivalente a ${descuento}
Subtotal con descuento: {subtotal_con_descuento}
Impuesto (16%): ${impuesto:.2f}
costo toal de la compra: ${costo_total_compra:.2f}

Gracias por hacer sus compras con nosotros!!!
""")
