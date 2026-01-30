print("5. Funciones")
print("Las funciones son bloques de cofigo reutilizables nos permiten encaptusalr tareas especificas y ejecutarlas cuando sea necesario. Las funciones nos ayudan a organizar nuestro codigo, evitar la repeticin y jacer que nuestros programas sean mas modulare sy faciles de mantener")
print("")

print("Definir una funcion")
print("Para definir una funcion en python, utilizamos la palabra clave def seguida del nombre de la funcion yparentesis. Opcionalmente, podemos especificar pará emtros dentro de lso paréntesis. El bloque de codigo de la funcion se indenta despues de los dos puntos.")
print("")

print("Para llamar a una funcion, simplemente escribimos el nombre de la funcion seguido de paréntesis:")
print("ejemplo:")
print("")

def saludo():
    print("¡hola, mundo!")

saludo()

print("")

print("PARÁMETROS Y ARGUMENTOS")
print("Las funciones pueden aceptar parámetros, que son vaores que se pasan a la funcion cuando se le llama. Los parámetros se especifican dentro de los parentesis en la deficion de la función.")
print("")
print("ejemplo:")
print("")

def saludo(nombre):
    print(f"!Hola, {nombre}!")

print("")

print("Al llamaar a la funcion, proporcionamos los argumentos correspondientes a los parámetros:")
print("")

saludo("Juan")
saludo("María")
print("")

print("VALORES DE RETORNO")
print("Las funciones pueden devolver valores utilizando la palabra clave return. el valor de retorno puede ser utilizado por el codigo que llama a la funcion")
print("")

def suma(a, b):
    return 2*a + b

resultado = suma(3, 4)
print(resultado)
print("")

print("FUNCIONES ANÓNIAMAS (LAMBDA)")
print("Python permite crear funciones anónimas o funciones lambda, que son funciones sin nombre definidas en una sola linea. Se utilizan comunmente para funciones pequeñas y concisas.")
print("")

cuadrado = lambda x: x**2
print(cuadrado(5)) #imprime 25
print("")

print("ALACANCE DE LAS VARIABLES (LOCAL VS. GLOBAL")
print("Las variables definidas dentro de una funcion tienen un alcance local, lo que signfica que solo son accesibles dentro de la funcion. Por otro lado, las variables definidas fuera de cualquier funcion teienen un alcance global y puden seraccedidas desde cualquier parte del programa.")
print("")

def funcion():
    variable_local = 10
    print(variable_local) #accesible dentro de la función

variable_global = 20

def funcion2():
    print(variable_global) #Accesible desde cualquier lugar

funcion() #imprime 10
print("")
funcion2() #mprime 20
print("")
print(variable_global) #imprime 20
print("(variable_local) #Gener un errro, la variable no está definida en este alcance.")

print("")

print("Inicio de video explicativo")

def calcular_media(*numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    return media

print("Media:", calcular_media(10, 20, 30, 40))
print("")

#----------------------------------------
print("Puedo expresar la funcion simple asi:")

def sumar_3(x):
    return x + 3

print("sumarle 3 a un numero:", sumar_3(5))
print("")

#----------------------------------------
print("O tambien puedo expresarla así:")

sumar_3 = lambda x: x + 3

print("sumarle 3 a un numero:", sumar_3(5))
print("")

print("cierre de video explicativo")
print("")

print("DOCUMENTACION DE FUNCIONES (DOCSTRINGS")
print("Es una buena practica documentar nuestras funciones utilzando docstrings. Los docstringss son cadenas de texto que desriben el proposito, los parámetros y el valor del retorno de una funcion. Se colocan inmedaietamente despues de la funcion y se encierran entre triples comillas dobles.")
print("")

def area_rectangulo(base, altura):
    """
    Calcula el area del rectangulo.
    
    Args:
        base (float): La base del rectangulo.
        altura (float): La altura del rectangulo
        
    Returns:
        float: El area del rectangulo.
    """
    return base * altura

print("Area del rectangulo:", area_rectangulo(5, 10))
print("")

print("En resumen, las funciones son una parte fundamental de la programacion en python. Nos permiten organizar nuestro codigo, reutilizar tareas especificas y mejorar la legibilidad de nuestros programas. Al comprender como definir, llamar y utilizar funciones, podemos escribir codigo mas eficiente y modular.")
print("")

print("FUNCIONES CON NUMERO VARIABLE DE ARGUMENTOS")
print("Python permite definir funcones que acepten un numero variable de argumentos. Esto se logra utilizando el operador * antes del nombre del parámetro.")
print("")

def suma_variable(*numeros): # numero recibe la tupla
    total = 0
    for numero in numeros: # iteras la tupla
        total += numero # es lo mimso a decir total = total + numero
    return total

print(suma_variable(1, 2, 3)) #imprime 6
print("")
print(suma_variable(4, 5, 6, 7)) #Imprime 22
print("")

print("Las funciones son una herramienta fundamenta en la programacion y nos permiten estrcuturar modularizar nuestro codigo. Con la capacidad de definir funciones personalizadas, podemos encapsular tareas específicas y reutilizarlas en diferentes partes de nuestro programa.")
print("")
print("Ademas de las funciones definidas por el usuario, Python tambien proporciona una amplia gama de funciones incorporadas que podemos utilizar directamente, como print(), len(), range, entre otras.")
print("")
print("Al dominar el uso de funciones, podemos escribir codigo mas limpio, eficiente y facil de mantener. ¡Sigue practicando y explorando las posibilidades que las funciones ofrecen en Python!")