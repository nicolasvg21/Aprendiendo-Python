"""
Docstring for python de Udemy.7. Sentencias de control.94. Aplicacion de salud y fitnes

Se solicita crear una aplciacion de salud y fitness que solicita lo siguiente:

- Nombre del susuario
- Pasos caminados en el dia

Ademas definiremoas las siguientes constantes:

META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado en kilocalorias

Con los valores anteriores debemos calcular las calorias quemadas segun los pasos caminados

calorias quemadas = pasos_diarios * CALORIAS_POR_PASO

y verificamos si se cumplio la meta de pasos diarios

meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
"""

print("*** APLICACION DE SALUD Y FITNESS ***")

# constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado en kilocalorias

# Pedimos los valores
nombre_usuario = input("Cual es tu nombre? ")
pasos_diarios = int(input("Cuantos pasos has caminado hoy? "))

# Verificar si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = "si" if meta_alcanzada else "No"

# Calculamos la calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la informacion
print(f"\nUsuario: {nombre_usuario}")
print(f"Pasos dados hoy: {pasos_diarios}")
print(f"Calorias quemadas: {calorias_quemadas}")
print(f"Meta de pasos diario alcanzada? {meta_alcanzada_txt}")
print(f"La meta de pasos diarios es de: {META_PASOS_DIARIOS}")