print("*** Imprimir del 1 al 5 de forma recursiva***")

# Definir la funcion recursiva
def funcion_recursiva(numero):
    # Caso base
    if numero == 1:
        print(numero, end=" ") # 1 
        
    else: # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=" ")
        
        
# programa principal
funcion_recursiva(5)

"""
Ya entendí esta verga, lo que sucede que cuando tengo esto:

        print(numero, end=" ")
        funcion_recursiva(numero - 1)

Se va a imprimir primero el numero y despues se regresará la función, pero si tengo esto:

        funcion_recursiva(numero - 1)
        print(numero, end=" ")

Se regresará a funcion antes de escribir el numero
"""