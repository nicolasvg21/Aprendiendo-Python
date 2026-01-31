print("7.. Entradas/Salidas")
print("En Python, la entrada y salida de datos nos permite interactuar con el usuario y manipular archivos. Podemos solicitar información al usuario, mostrar resultados en la pantalla y leer o escribir datos en archivos externos.")
print("")

print("ENTRADA DE DATOS DEL USUARIO")
print("Para obtener información del usuario durante la ejecución del programa, podemos utilizar la función input(). Esta función muestra un mensaje en la pantalla y espera a que el usuario ingrese un valor.")
print("")

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad ")

print("")

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

print("")

print("En este ejemplo, se solicita al usuario que ingrese su nombre y edad utilizando la función input(). Los valores ingresados se almacenan en las variables nombre y edad, respectivamente. Luego, se utilizan estas variables para mostrar un saludo personalizado en la pantalla.")

print("")

print("IMPORTANTE")
print("La fucion input() siempre devuelve una cadena de texto. Si deseas trabajar con otros tipos de datos, como números enteros o flotantes, debes realizar una conversión explícita utilizando funciones como int() o float().")

print("")

edad = int(input("Ingres tu edad: "))

print("")

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

print("")

print("En este ejemplo, se solicita al usuario que ingrese su edad y se convierte el valor ingresado a un número entero utilizando int(). Luego, se utiliza una estructura condicional para verificar si la edad es mayor o igual a 18 y mostrar un mensaje correspondiente.")

print("")

print("SALIDA DE DATOS")
print("Para mostrar información en la pantalla, utilizamos la función print(). Esta función toma uno o más argumentos y los muestra en la consola.")
print("")
print("Podemos utilizar la f-string (formateo de cadenas) para incrustar variables directamente dentro de una cadena de texto.")
print("")

nombre = "Juan"
edad = 25

print(F"hola, mi nombre es {nombre} y tego {edad} años.")

print("combiandolo con las entradas de arriba queda algo asi:")
print("")

nombre = input("ponga su triple hpta nombre: ")
edad = int(input("ponga su triple hpta edad: "))

print(F"hola, mi nombre es {nombre} y tego {edad} años.")

print("")

print("En este caso, las variables se incrustan dentro de la cadena utilizando llaves {} y se precede la cadena con la letra f para indicar que es una f-string.")