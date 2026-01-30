print("MANEJO DE EXCEPCIONES")
print("El manejo de excepciones nos permite caputarr y manejar errores de manejar controlada utilizando las declaraciones try, except y opcionalmente finally.")
print("")

print("Try")
print("El bloque try contrine el codigo que puede genear una excepcion. Si ocurre una excepcion dentro del bloque try, el flujo de ejecucon se transfiere al bloque except crrespondiente.")
print("")

try:
    # Codigo que puede generar una excepcion
    resultado = 10 / 0 # Division por 0
    print(resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
print("")

print("Except")
print("El bloque except especifica el tipo de excepcion que se desea capturar y manejar. Puedes tener multriples bloques except para manejar diferentes tipos de excepciones.")
print("")

try:
    # Codigo que se puede genera una expcepcion
    resultado = 10 / 0 # Division por 0
    print(resultado)
except ZeroDivisionError:
    print("Error: Division por cero")
except ValueError:
    print("Error: Valor invalido")

print("")

print("Finally")
print("El bloque finally es opcional y se ejecuta siempre, independientemente de si ocurrio una excepcion o no. Se utiliza comunmente para realizar tareas de limpieza o liberacion de recursos.")
print("")

try:
    # Codigo que puede genenrar una excepcion
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close() # Cerrar el archivo siempre, incluso si ocurrer una excepcion