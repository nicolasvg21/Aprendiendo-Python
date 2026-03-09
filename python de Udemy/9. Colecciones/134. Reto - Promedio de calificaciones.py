"""
Promedio de califiaciones

Crear un programa para realizar el calculo promedio de califiaciones.

El programa debe solicitar el numero de califiacion a utilizar apra obterner el promedio

Posteriomente, se debe solicitar cad califiacion al susuario

Posterioemtne realizar la suma de todas las calificaciones y finalmente mandr a imprimir el promedio.
"""
print("*** Promedio de califaiciones ***")

lista_calificaciones = []
sumatoria = 0
numero_calificaciones = int(input("Proporciona el numero de calificaciones a evaluar: "))

for sistema in range(numero_calificaciones):
    calificacion = float(input(f"Calificación[{sistema}] = "))
    sumatoria += calificacion
    lista_calificaciones.append(calificacion)

print(f"\nLas calificaciones proporcionadas son: {lista_calificaciones}")

print(f"La suma de todas las calificaciones es: {sumatoria}")
promedio = sumatoria/numero_calificaciones

print(f"Promedio de las califiaciones: {promedio}")

print("****** MI PROFE LO HACE ASÍ  *****") #------------------------

total_calificaciones = int(input("proporciona el numerod ecalificaciones a evaluar: "))
calificaciones = []

# Iterar las acalifaciones 
for indice in range(total_calificaciones):
    calificacion = float(input(f"Califiaciones[{indice}] = "))
    calificaciones.append(calificacion)

# Imprimimos las califiacione sproporionadas
print(f"\nLas califiaciones proprpocionadas son: {calificaciones}")

# Calculamos el promedioo de las califaiciones
# sum(iteracble)
suma_califaiciones = sum(calificaciones)
promedio = suma_califaiciones / total_calificaciones
print(f"\nPromedio de las califiaciones: {promedio:.2f}")