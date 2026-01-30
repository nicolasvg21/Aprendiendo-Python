print("3.1. BUCLES /LOOPS")
print("Los bucles nos permites repetir un bloque de codigo varias vece. En pyhon , los bucles mas comunes son for y while.")
print("")

print ("FOR")
print("Se utiliza para iterar sobre una secuencia (como una lsita, una tupla o una cadena o cualquier objeto iterable. La sisntaxis basica es la siguiente:")
print("")

print("for varible in secuencia:")
print("    #Bloque de codigo a repetir")
print("    instrucciones")
print("")

print("ejemplo")
print("Iterar sobre una lista de frutas:")
print("")

print("frutas  = [\"manzana\", \"banana\", \"naranja\"]")
frutas=["manzana","banana","naranja"]

for fruta in frutas:
    print(fruta)
print("")

print("En este ejemplo, el bucle for itera sobre la lista furtas. En cada iteracion, la variable frutas toma el valor de un elemento de la lista,  se ejecuta el bloque del codigo dentro del bucle. En este caso, se imprime cada fruta en la linea separada.")
print("")

print("WHILE")
print("El bucle whule se utiliza para repetirun bloque de codigo mientras una condicion sea verdadera. Ña sisntaxis asica es la siguiente:")
print("")

print("while condicion:")
print("    #Bloque de codigo a repetir")
print("    instrucciones")
print("")

print("ejemplo:")
print("")

contador = 0

while contador < 5:
    print(contador)
    contador += 1
print("")

print("En este ejempplo, el bucle while se ejecuta mientras la variable contador sea menor que 5. Enn cada iteracion, se imprime el valor de contador, luego se incrementa 1 meidante la instruccion contador += 1. El bucle se detendrá cuando contador alance el valor de 5.")
print("")
print("Es importante tener en cuidado al usar el bucle while, ya que, si la condicion nunca se vuelve falsa, el bucle se ejecutará indefinidamente, l oque se conoce como un bucle infinit.")
print("")

print("Numero del 1 al 5 multiplicados por 2 con blucle for:")
for numero in range(1,6):
    print(numero*2)
print("")

print("\nNumero del 1 al 5 multiplicados por 2 con bucle while:")

contador = 0

while contador <5:
    print (contador*2)
    contador += 1
print("")


print("CONTROL DE BLOQUES")
print("Python proporciona algunas instrucciones especiales para controlar el flujo de ejecucion dentro de los bucles.")
print("")

print("BREAK")
print("La instruccion break se utiliza para salir prematurametne de un bucle, independeintemente de la condición, cuando se encuentra un break, el bucle se deteniene y el flujo de ejecucion continua con la siguiente instruciión")
print("")
print("ejemplo:")
print("")

contador = 0

while True:

    print(contador)
    contador += 1

    if contador == 5:
        break
print("")

print("En este ejemplo, el bucle while se ejecuta indefinidamente debido a la condicion True. Sin embargo, dentro del bucle se utiliza la estructura condicional if para vergicar si contador es giual a 5. Cuando se cumple esta codicion, se ejecuta la instruccion break, lo que hace que el bucle se detenga y el flujo de ejecucion continue con la siguiente isntruccion del bucle")
print("")


print("CONTINUE")
print("esta instruccion se utiliza para saltar el resto del bloque de codigo dentro de un bucle y pasar a la siguiente iteración")
print("")

print("por ejemplo en el siguiente ejemplo se utilizó el operadro módulo % 2, si el numero es divisible por 2, es decir par, se ejecuta la instruccion continue, lo que hace que se salta el resto del bloque de codigo y se pase a la siguietne iteracion del bucle, Como resultado solo se imprimiran los numeros impares")

for i in range(10):
    if i % 2 == 0:
        continue 
    print(i)
print("")

print("PASS")
print("la intrucion pass es una operacion nula que no hace nada. Se utiliza como marcador de poscion cuando se requiere una instruccion sintactica, pero no se desea realizar ninguna acción:")
print("")
print("ejemplo:")
print("")

for i in range(5):
 pass

print("En este ejemplo, el bucle for itera sobre los numero del 0 al 4, pero no se realiza ninguna accion dentro del bucle debid a la instruccion pass. Esto puede ser util cuando se está desarrollando un programa y se desea reservar un bloque de condigo para mplementarlo mas adelante")
