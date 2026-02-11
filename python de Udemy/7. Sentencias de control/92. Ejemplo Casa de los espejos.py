"""
Docstring for python de Udemy.7. Sentencias de control.92. Ejemplo Casa de los espejos

CASA DE LOS ESPEJOS

Suón que estás en un parque de diversiones y quiers entrar a la csa de los espejos.

Sin embargo debes cumplir con algunas condciones.

1. Debes tener mas de 10 años
2. No debe darte miedo la oscuridad

Si se cumplen las condiciones anteriores puedes entrar.

Para realizar este ejemplo vamos a utilizar el operador not para apllicar una logica inversa
"""

print("*** BIENVENIDOS A LA CASA DE LOS ESPEJOS ***")

edad = int(input("Cual es tu edad? "))
tienes_miedo_oscuridad = input("Tienes miedo a la oscuridad (Si/No)? ")
tienes_miedo_oscuridad = tienes_miedo_oscuridad.strip().lower() == "si"

if not tienes_miedo_oscuridad and edad >= 10:
    print("\nPuedes entrara a la casa de los espejos")
else:
    print("\nLo siento, la casa de lso espejos podria darte miedo")