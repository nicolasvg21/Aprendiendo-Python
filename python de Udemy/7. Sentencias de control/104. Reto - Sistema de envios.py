"""
Docstring for python de Udemy.7. Sentencias de control.104. Reto - Sistema de envios

sistema de envios

Crea un programa para determinar el costo de envio de un paquete segun el destino (naciional o internacional) y el peso del paquete

costo tarifas:
Nacional = 10 * kilo
internacional = 20 * kilo

El programa debe solicitar 2 valores:
1) Destino (nacional o internacional)
2) Peso (kilogrmamos) del paquete

Al final debe imprimir el costo de envio del paquete
"""

destino = input("Ingresa por favor el lugar de estino: ")
destino = destino.strip().lower()
peso = float(input("Escribe el peso en kilogramos de tu paquete: "))

if destino == "nacional":
    costo_peso = peso * 10
elif destino == "internacional":
    costo_peso = peso * 20
else:
    print("Maldita sea le pido que me diga si es nacional o internacional")

print(f"\nEl detino que seleccionaste fue {destino} y el peso de tu paquete es de {peso} kilogramos por ende el costo de tu envio es de ${costo_peso:.2f} dolares")
