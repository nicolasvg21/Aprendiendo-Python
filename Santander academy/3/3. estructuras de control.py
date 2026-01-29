print("ESTRUCTURAS DE CONTROL")
print("Las estructuras de control nos permiten controla el flujo de ejecucion de nuestros programas. En el python, las estructuras de control mas comunes son las estructuras condicinales  ylos blucles. Estas estructuras nos permiten tomar decisiones y repetir bloques de codigo segun ciertas condiciones.")
print("")

print("Estructuras condicionales")
print("Las estructuras condicionales nos permiten ejecutar diferentes bloques de codigo segun se cumpla o no una determinada condicion. En Pyhton, las estructuras condicionales mas utilizadas son if, if-else y if-elif-else.")
print("")

print("IF")
print("La estructura if se utiliza para ejecutar un bloque de codigo si una condicion es verdadera. La sintaxis basica es la siguiente:")
print("")

print("if condicion:")
print("    #Bloque de codigo a ejecutar si la condicion es verdadera")
print("    instrucciones")
print("")

print("ejemplo")
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
print("")

print("En este ejemplo, si la variable edad es mayor o igual a 18, se ejecutará el bloque de codigo dentro del if y se impimirá el mensaje \"Eres mayor de edad.\"")
print("")

print("IF-ELSE")
print("La estructura de if-else nos permite especificar un bloque de codigo alternativo que se ejecutará si la condicion del if es falsa. La sintaxis básica es la siguiente:")
print("")

edad = 15 

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
print("")

print("En este ejemplo, si la variable edad es mayor o igual a 18, se ejecutará el bloque de codigo dentro de if y se impimirá el mensaje \"Eres mayor de edad.\" De lo contrario, se ejecutará el bloque de codigo dentro del else y se imprimirá el mensaje \"Eres menor de edad\".")
print("")

print("IF-ELIF-ELSE")
print("La estructura if-elif.else nos permite especificar multiples condiciones y bloques de codigo alternativos. La sintaxis basica es la siguiente:")
print("")

print("if condicion1:")
print("")

print("    #Bloque de codigo a ejecutar si la condicion1 es verdadera")
print("    instrucciones")
print("")

print("elif condicicion2:")
print("")

print("    #Bloque de codigo a ejecutrar si la condicion2 es verdadera")
print("    instrucciones")
print("")

print("else:")
print("    #Bloque de codigo a ejecutar si ninguna condicion anterior es vedadera")
print("    instrucciones")
print("")

print("- ejemplo")

calificacion = 20 

if calificacion >= 90:
    print("Excelente")

elif calificacion >= 80:
    print("Muy bien")

elif calificacion >= 70:
    print("Bien")

else:
    print("Necesitas mejorar")
print("")

print("En este ejemplo se evaluan mutiples condiciones en orden. Si la variable calificaciones es mayor o igual a 90, se imprime \"Excelente\". Si no se cumple la primera condicion, pero calificacion es mayor o igual a 80, se imprime \"Muy bueno\". Si no se cumplen las condiciones anteriore, pero califiacion es mayor o igual a 70, se imprime \"Bueno\". Si ninguna de las condiciones antteriores es verdadera, se ejecutaá el bloque else y se imprime \"Necesita mejorar\"")
print("")

print("- Ejercicio propuesto")
print("Escribe un programa que solicite al usuario su edad y determine si es menor de")

edad = 10

if edad < 18 and edad > 0:
    print ("Eres menor de edad")

elif edad >= 18 and edad < 60:
    print ("Eres un adulto.")

elif edad == 60:
    print("Feliz cumpleaños!")

elif edad > 60:
    print("Eres un adulto mayor")
    
else:
    print("papi es imposible que le de error este mlp programa")
    