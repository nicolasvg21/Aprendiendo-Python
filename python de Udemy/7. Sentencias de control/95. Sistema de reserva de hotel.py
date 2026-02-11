"""
Docstring for python de Udemy.7. Sentencias de control.95. Sistema de reserva de hotel

SISTEMA RESERVA HOTEL

Se solicita crear un sistema de reservacion de un hotel.
Se debe pedir la siguiente informacion al usuario:
- Nombre de cliente
- Dias de estadia en el hotel
- Cuarto con vista al mar?

El hotel tiene las siguientes tarifas:

- Cuarto sin vista al mar: $150.50 por dia
- Cuarto con vista al mar: $190.50 por dia

El sistema debe calcular el costo total de la estadia dependiendo si eligio un cuarto con vista al mar o no.
Ademas debe indicar si escogió un cuarto con vista al mar o no.
"""

print("*** SISTEMA DE RESERVA DE HOTEL ***")

CUARTO_CON_VISTA = 190.5 #por dia
CUARTO_SIN_VISTA = 150.5 #por día

nombre_cliente = input("cual esl nombre de quien alquila? ")
tiempo_estadia = int(input("Cuantos dias desea hospedarse? "))
vista_cuarto = input("Desea un cuarto con vista al mar? (Si/No) ").strip().lower()
costo_dia_con = tiempo_estadia * CUARTO_CON_VISTA
costo_dia_sin = tiempo_estadia * CUARTO_SIN_VISTA

print("\n----------- DETALLES DE LA RESERVACION --------------")
print(f"El nombre de quien alquila es: {nombre_cliente}")
print(f"Dias a hospedarse: {tiempo_estadia}")
if vista_cuarto == "si":
    print(f"El precio total es de {costo_dia_con}")
else:
    print(f"El precio total es de {costo_dia_sin}")

print("--------- SISTEMA DE RESERVA DEL PROFE ---------")

# variables del horel
tarifa_diaria_sin_vista_mar = 150.50
tarifa_diaria_con_vista_mar = 190.50

# Pedimos la informacion al usuario
nombre_cliente = input("Nombre del cliente: ")
dias_estadia = int(input("Dias de estadia: "))
vista_al_mar_txt = input("Con vista al mar (si/no) ")
vista_al_mar = vista_al_mar_txt.strip().lower() == "si"

# Costo total de la estancia
if vista_al_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista_mar
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista_mar

# Mostramos los detalles de la reserva
print("\n---------------- Detalles de la reservación-----------")
print(f"""
cliente: {nombre_cliente}
dias de estadia: {dias_estadia} 
costo total: ${costo_total:.2f}
Habitacion con vista al mar: {"si" if vista_al_mar else "no"}""")
