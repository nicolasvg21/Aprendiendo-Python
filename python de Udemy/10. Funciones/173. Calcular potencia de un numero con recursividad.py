"""
Potencia de un numero usando funciones recursivas

Calcular la potencia de un numero usando una funcion recursiva

La formula es: a^b= a * a^(b-1)

Donde a es la base y b la potencia, lo que significa multiplicar a por si mismo b veces

ej: 

2^3 = 2*2*2 = 8 
6^2 = 6*6 = 36
4^5 = 4*4*4*4*4 = 1024

El caso base, exponente == 0
"""
print("*** Potencia de un numero usando funciones recursivas ***")

# Definimos la funcion potencial recursiva
def potencial_recursiva(potencia):
    # Como base, potencia de 0 = 1
    if potencia == 0:
        print(f"Resultado de la potencia de {base}^{potencia} = 1")
        return 1
    
    else: # Caso recursivo
        potencial_parcial = base * potencial_recursiva(potencia - 1)
        print(f"Resultado potencial parcial de {base}^{potencia} es: {potencial_parcial} ")
        return potencial_parcial

base = 2
potencia = 4
resultado = potencial_recursiva(potencia)
print(f"\nEl resultado final de {base}^{potencia} = {resultado}")
print()
print()

print("*** asi lo hace mi profe ***") # --------------------------------

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    
    else: # Caso recursivo
        return base * potencia(base, exponente-1)
    
print(f"2 elevado a la 3: {potencia(2, 3)}")
print(f"5 elevado a la 0: {potencia(5, 0)}")
print(f"4 elevado a la 5: {potencia(4, 5)}")

