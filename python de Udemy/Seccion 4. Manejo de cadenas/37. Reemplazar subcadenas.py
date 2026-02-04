# Programa: Reemplaar textos en python
 
mensaje = "Hola Mundo, Mundo"

# Reemplazar TODAS las aparienciones
nuevo = mensaje.replace("Mundo", "Python")
print(nuevo)
# Salida: "Hola python, python"

# Reemplazar solo UNA vez

uno_solo = mensaje.replace("Mundo", "Dev", 1)
print(uno_solo)
# Salida: "Hola Dev, Mundo"