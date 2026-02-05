"""
Docstring for python de Udemy.5. Entrada de datos.py.53. Reto - Generador de Id Unico

Con los datos recbidos el sistema deberá realizar lo siguiente:

1. Del valor recibido de nombrem usar solo 2 primeras letras y convertirlas a mayusculas

2. Del valor de apellido, usar las 2 primeras letras y convertirlas a mayusuclas

3. Del valor de año, tomar los 2 ultimos digitos

Ademas el sistema deberá generar un valor aleatorio de 4 digitos con ayuda de la funcion randint

Finalmente, con los datos obtenidos enerar nu ID unico uniendo los valores como sigue
"""
import random

nombre = input("Escribe tu nombre: ")
nombre2p = nombre[0:2].upper()
print(f"Las dos primeras letras de su nombre son: {nombre2p}")

apellido = input("\nEscribe tu apellido: ")
apellido2p = apellido[0:2].upper()
print(f"Las dos primeras letras de su apellido son: {apellido2p}")

anio = str(input("\nCual es tu año de nacimiento: "))
anio2u = anio[2:4] # o tambien se puede dejar [2:]
print(f"Los 2 ultimos numeros de su año de nacimiento es: {anio2u}")

numeroAl1 = str(random.randint(0, 9))
numeroAl2 = str(random.randint(0, 9))
numeroAl3 = str(random.randint(0, 9))
numeroAl4 = str(random.randint(0, 9))
numeroAlT = numeroAl1 + numeroAl2 + numeroAl3 + numeroAl4

idUnico = nombre2p+apellido2p+anio2u+numeroAlT

print(f"""\n Hola {nombre}
      El resultado de su ID unico es: 
      {idUnico}
      Felicidades!!!!
""")
