"""
Docstring for python de Udemy.7. Sentencias de control.102. Reto - Sistema de calificaciones

SISTEMA DE CALIFICACIONES

Crear un programa para convertir una calificacion numerica (entre 0 y 10) a una letra (de la F a la A)

- Si es mayor o igual a 9 y menor o igual a 10 es una A
- Si es mayor o igual a 8 y menor a 9 es una B
- Si es mayor o igual a 7 y menor a 8 es una C
- Si es mayor o igual a 6 y menor a 7 es una D
- Si es mayor o igual a 5 y menor a 6 es una E
- Si es mayor o igual a 4 y menor a 5 es una C
- En otro casi, imprmir "valor desocnocido
"""

nota = int(input("Ingresa el valor de la nota: "))

if nota >= 9 or nota <= 10:
    calificacion = "A"
elif nota >= 8 or nota < 9:
    calificacion = "B"
elif nota >= 7 or nota < 8:
    calificacion = "C"
elif nota >= 6 or nota < 7:
    calificacion = "D"
elif nota >= 5 or nota < 6:
    calificacion = "E"
elif nota >= 0 or nota < 5:
    calificacion = "F"
else:
    calificacion = "trateme serio le digo una nota entre 0 y 10"

print(f"Como su nota fue de {nota} su califiacion final es {calificacion}")
    
