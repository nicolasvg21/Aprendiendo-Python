"""
Docstring for python de Udemy.5. Entrada de datos.py.48. Ejemplo entrada de datos
"""
nombre = input("Proporciona tu nombre: ")
print(f"tu nombre es: {nombre}")

# Cuidado con la conversionde tpos al trabajar con valores numericos
# Forma correcta: Envolver con int() o float()

# Para enteros (edad, cantidad)
edad = int(input("Tu edad: "))
print(f"Tu edad es: {edad}")
print(edad + 5) # ¡Funciona! (20 + 5 =25)

# Para decimales (precio, altura
altura = float(input("Tu altura es: "))
print(f"Tu altura es: {altura * 1/2:.3f}")
