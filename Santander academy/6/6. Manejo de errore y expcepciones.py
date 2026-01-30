print("MANEJO DE ERRORES Y EXCEPCIONES")
print("Cuando escribimos programas, es comun encontrarnos con situaciones ineseradas o errores durante la ejecucion. Python proporciona un mecanismo par amejar estos errores de manera controlada utilizando el manejo de excepciones. Esto nos permite capturar y manejar errores especificos sin que el progrmaa se detenga abruptamente.")
print("")

print("Errores comunes en python")
print("Antes de sumergirnos en el manejo de excepcones, veamos algunos erroes comunes que puedes encontrar en python")
print("")

print("Eror de sintaxis (syntaxError)")
print("Ocurre cuando el codigo no sigue las reglas de sintaxis de pyhon, como olvidadr dos puntos despues de una declaracion de funcion o bucle.")

def mi funcion () #Falta los puntos
    print("Hola")

print("")

print("Error de nombre (NameError)")
print("ocurre cuando se hace referencia a una variable o funcion que no ha sido definida.")

print("")

print(variable_no_definida) #claro error
print("Clarisimo error")

print("")

print("Error de tipo (TypeError)")
print("Oocurre cuando se realiza una operacion con tipos de datos incompatribles, como interntar sumar numeros y una cadena.")
print("")

resultado = 5 + "10"

print("")

print("Error de indice (IndexError)")
print("Ocurre cuando se intenta acceder a un indice fuera del rango valido de una lista o secuencia.")

lista = [1, 2, 3]
print(lista[3]) #El indice 3 está fuera del rango
print("")

print("Estos son solo algunos ejemplos de errores comunes. Cuando ocurre un error, python genera una excepcion y muestra un mensaje de error que incluye el tipo de excepion y una descripcion del problema.")
