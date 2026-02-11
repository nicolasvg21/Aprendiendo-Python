"""
Docstring for python de Udemy.7. Sentencias de control.99. Reto - Estacion del año

Identifica laestacion del año

Se solicita proporcionar el valor de un mes (valor numerico entre 1 y 12, e indicar la estacion del año segun lo siguiente:

Mes 1,2 o 12         -> invierno
mes 3, 4 o 5         -> primavera
mes 6, 7 o 8         -> verano
mes 9, 10 u 11       -> otoño
cualquier otro valor -> una estacion desconocida
"""

mes = int(input("ingresa el indicativo del mes entre 1 y 12: ").strip().lower())
estacion = None
print(type(mes))
#revision del mes proporconado
if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes ==6 or mes == 7 or mes == 11:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else:
    estacion = "Estacion desconocida"

# Imrprimir el resultado
print(f"La estacion para el mes {mes} es {estacion}")




