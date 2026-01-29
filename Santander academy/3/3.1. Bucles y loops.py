print ("FOR se utiliza par aiterar sobre una secuencia (como una lsita, una tupla o una cadena o cualquier objeto iterable. La sisntaxis basica es la siguiente:")

frutas=["manzana","banana","naranja"]

for fruta in frutas:
    print(fruta)

print("Numero del 1 al 5 multiplicados por 2 con blucle for:")
for numero in range(1,6):
    print(numero*2)


print("#WHILE se utiliza para repetir un bloque de codigo mientras una condicin sea verdaera. La sintaxis basica es la siguiente:")

contador = 0

while contador <5:
    print (contador)
    contador += 1

print("CONTROL DE BLOQUES")
print("Break e utiliza para salir prematurametne de un bucle, independeintemente de la condición, cuando se encuentra un break, el bucle se deteniene y el flujo de ejecucion continua con ula siguiente instruciió")

contador = 0

while True:

    print(contador)
    contador += 1

    if contador == 5:
        break



print("\nNumero del 1 al 5 multiplcados por 2 con bucle while:")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

print("CONTINUE esta instruccion se utiliza para saltar el resto del bloque de codigo dentro de un bucle y pasar a la siguiente iteración")
print("por ejemplo en el siguiente ejemplo se utilizó el operadro módulo % 2, si el numero es divisible por 2, es decir par, se ejecuta la instruccion continue, lo que hace que se salta el resto del bloque de codigo y se pase a la siguietne iteracion dl bucle, Como resultado solo se imprimiran los numeros impares")

for i in range(10):
    if i % 3 == 0:
        continue 
    print(i)

print("PASS la intrucion pass es una operacion nula que no hace nada. Se utiliza como marcador de poscion cuando se requiere una instruccion sintactica, pero no se desea realizar ninguna acción:")

for i in range(5):
 pass
