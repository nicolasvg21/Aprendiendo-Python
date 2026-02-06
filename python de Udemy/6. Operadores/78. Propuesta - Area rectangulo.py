"""
Docstring for python de Udemy.6. Operadores.78. Propuesta - Area rectangulo

CLCULO AREA Y PERIMETRO DE UN RECTANGULO

Se solicita calcular el area y perimetro de un rectangulo aplicando las siguientes formulas:
-------------------------------
|                              |
|                              |
|                              | altura
|                              |
|                              |
--------------------------------
                base

area = base * altura
perimetro = 2 * (base + altura)
"""

print("****** Calculo de area y perimetro de rectangulo *******")

base = float(input("\nindique la base del rectangulo: "))
altura = float(input("\nIndique la altura del rectangulo: "))

area = base * altura
perimetro = 2*base + 2*altura

print(f"\nel rectangulo posee un area de {area:.2f} y un perimetro de {perimetro:.2f}")