"""
python de Udemy.20. Reto - Ejercicio de reserva de hoteles

Crea un sistema de reserva de hoteles que contenga la siguiente informacion de una reserva:

- Nombre del cliente
- Dias de estancia
- tarifa diaria
- Indicar si el cuarto tiene vista al mar


Despues mandar a imprimir los valores de cada variable

El resultado del sistema debe ser el siguiente:

*** sistema de reserva de hoteles ***
Cliente: Laura Martinez
Dias de estancia: 5
terifa dairia: 1200.0
Habitacion con vista al mar? True
"""

# Desarrollo de problema

nombre_cliente = "Laura Martinez"
dias_estancia = 5
costo_diario = 1200.0
tiene_vista_mar = True

print("Nombre de quien reserva:", nombre_cliente)
print("¿Cuantos dias se va a quedar?", dias_estancia)
print("Precio de la estadia por dia:", costo_diario)
print("¿Su habitacion tiene vista al mar?", tiene_vista_mar)
print()

#cambios a las variabes a ver si funciona

nombre_cliente = "Nicolas Vargas"
dias_estancia = 30
costo_diario = 500.99
tiene_vista_mar = False

print("Nombre de quien reserva:", nombre_cliente)
print("¿Cuantos dias se va a quedar?", dias_estancia)
print("Precio de la estadia por dia:", costo_diario)
print("¿Su habitacion tiene vista al mar?", tiene_vista_mar)