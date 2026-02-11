"""
Docstring for python de Udemy.7. Sentencias de control.81. Sentencias de decision
"""
print("*** SENTENCIA IF ***")
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print(f"Eres mayor de edad, tienes {edad}")
elif 13 <= edad <18:
    print(f"Tienes {edad} años de edad, puede que estés en preparatoria")
else:
    print(f"Tienes {edad} años de edad, no puede contratar una prostituta")