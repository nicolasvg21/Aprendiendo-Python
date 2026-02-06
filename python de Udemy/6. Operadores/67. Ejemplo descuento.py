"""
Docstring for python de Udemy.6. Operadores.67. Ejemplo descuento

SISTEMA DESCUENTOS VIP

Una tienda de supermercado ofrece un descuento especial a clientes que compren 10 o mas articulos por dia y ademas sean miembro de la tienda.

El sistema debe solicitar al cliente que indique cuantos articulos ha comprado en el dia y preguntele si cuenta con memebresia de la tienda.

En caso de haber coprado 10 o mas productos y ser miembro de la tienda entonces trendrá acceso al descuento VIP
"""

print("**** SISTEMA DE DESCUETOS VIP ****")

N0_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input("\nCuantos productos compraste hoy?"))
tiene_membresia = input("\nTienes la membresia de al tienda (Si/No)")

es_elegible_descuento = (cantidad_productos >= N0_PRODUCTOS_DESCUENTO and tiene_membresia.strip().lower() == "si")

print(f"\nTienes acceso al descuento VIP: {es_elegible_descuento}")