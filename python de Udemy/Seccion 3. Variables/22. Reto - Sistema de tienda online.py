"""
Docstring for python de Udemy.22. Reto - Sistema de tienda online

Crea el detalle de un producto de una teinda online 

El detalle del producto debe tener:

- Nombre del producto
- Precio del productoo
- Cantidad en el inventario
- Indicar si está disponible

Hacer algunos cambios y manda a imprimir nuevamente el nuevo valor de las variables

El resultado debe ser similar al siguiente:

*** Sistema de tienda online ***
Producto: Camara digital
Precio: $399.99
Cantidad inventario: 20
Disponible: True
"""

# Definir las variables de un producto

producto = "Cámara digital"
precio_prodcuto = 399.99
cantidad_stock = 20
producto_disponible = True

print("*** SISTEMA TIENDA ONLINE ***")
print("¿Que producto desea llevar?", producto)
print("El precio de este producto es:", precio_prodcuto)
print("En inventario:", cantidad_stock)
print("Disponibilidad:", producto_disponible)

# Hacemos algunos cambios
precio_prodcuto = 299.99
cantidad_stock = 10
producto_disponible = True

print()
print("*** SISTEMA TIENDA ONLINE ***")
print("¿Que producto desea llevar?", producto)
print("El precio de este producto es: $", precio_prodcuto)
print("En inventario:", cantidad_stock)
print("Disponibilidad:", producto_disponible)
