"""
Docstring for python de Udemy.8. Ciclos.120. Reto - Juego de adivinar

Juego de adivinanzas

Crea un juego donde el jugador debe adivinar un numero secreto.

Puedes usar un ciclo while hasta que el jugador adivine correctametne.

El numero secreto se puede crear usando la funcion dandint para generar un valor aleaorio entre 1 y 50

Por cada intento fallido se debe incrementar una varible que lleve el conteo de intentos

El programa debe orientar al jugador incidcandoel si el valor que proporciono fue mayor o menor que el numero secreto

Finalmente si adivina el numero ecreto debe felicitar al usuario e indicar intentos realizó

Opcionalmente, se pued elimitar el juego a un numero de intentos maximos (ej: 10) de lo contrario continua el juego.
"""

print("*** Juego de adivinanzas ***")

intento = 1
import random
numero = random.randint(1, 50)
print(numero)
num_usuario = int(input("Intenta adivinar el numero entero entre el 1 al 50: "))
salir = True
while salir:
    if numero != num_usuario and intento <= 10:
        if num_usuario < numero and 1 <= num_usuario <= 50 :
            print(f"\nEste es el intento: {intento}")
            print(f"\nEl numero {num_usuario} es menor al objetivo, intentalo de nuevo")
            intento += 1
            num_usuario = int(input("\nIntenta adivinar nuevo el numero: "))
        elif num_usuario > numero and 1 <= num_usuario <= 50 :
            print(f"\Este es el intento: {intento}")
            print(f"\nEl numero {num_usuario} es mayor al objetivo, intentalo de nuevo")
            intento += 1
            num_usuario = int(input("\nIntenta adivinar nuevo el numero: "))
        else:
            print(f"\nEste es el intento: {intento}")
            print("\nchupelo estoy siendo bien claro re mlp, entero entre 1  a 50")
            intento += 1
            num_usuario = int(input("\nIntenta adivinar nuevo el numero: "))
    elif intento == 11:
        print("\nPerro ud es muy bruto la plena como se gasta los 10 intentos y no da con el numero")
        salir = False
    else:
        print(f"\nParce por fin dio con el numero {numero} al intento {intento} ud ya no es tan bruto")
        salir = False
else:
    print("\nSaliendo del juego")

print("*** ASÍ LO HACE MI PROFE ***")

from random import randint

numero_secreto = randint(1, 50)
intentos = 0
adivinanza  = None
INTENTEOS_MAXIMOS = 5

while adivinanza != numero_secreto and intentos < INTENTEOS_MAXIMOS:
    adivinanza = int(input("Adivina el numero secreto (1, 50): "))
    # Agregamos una ayuda para orientar al jugador:
    if adivinanza < numero_secreto:
        print("El numero secreto es mayor")
    elif adivinanza > numero_secreto:
        print("El nummero secreto es menor")
    # Incrementamos la variable de intentos
    intento += 1
# conclusion del juego
if adivinanza == numero_secreto:
    print(f"Felicitaciones le atinaste en el intento {intento}")
else:
    print(f"Lo siento, has agotado tus intentos maximos: {INTENTEOS_MAXIMOS}")
    print(f"El numero secreto era: {numero_secreto}")
