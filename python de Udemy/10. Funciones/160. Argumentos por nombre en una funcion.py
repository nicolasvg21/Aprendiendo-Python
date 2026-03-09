print("** Funcion con argumentos or nombre ***")

def imprimir_persona(nombre, apellido=" ", edad=0):
    print(f"Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}")

# Primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona("Ricardo", "Quintana", 32)

# Llammar la funcion usando argumentos por nombre
imprimir_persona(nombre="Carlos", apellido="Rojas", edad=28)

# Llamar la funcion usando argumentos pornombre, pero intercambiando el orden
imprimir_persona(edad=28, apellido="Rojas", nombre="Carlos")

# Argumentos con valor por defaul, convierte a los valores en opcionales, es este caso, vamos a unicamente solicitar a la persona que coloque su nombre para que entonces quede el apellido como cadena vacia apellido=" " y la edad quede con el valor de 0 edad=0
imprimir_persona(nombre="Carlos")

# Como dejamos claro que el apellido y la edad son opcionales, eso no quita la opcion de reescribir el código e intercambiarlos
imprimir_persona(nombre="Carlos", apellido="Rojas")
imprimir_persona(apellido="Rojas", nombre="Carlos")