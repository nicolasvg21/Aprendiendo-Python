"""
Docstring for python de Udemy.5. Entrada de datos.py.45. Ejemplo de la funcion de bool
"""

#1. Numeor (int y float)
print(bool(0))      # False (El vacio numerico)
print(bool(0.0))    # False
print(bool(42))     # True (existe valor)

# 2. Texto ( strings)
# Cadena  vacia = Nada = False
print(bool(""))     # False

# Cadena con espacio o texto = Algo = True
print(bool(" "))    # True
print(bool("Hola")) # True

# 3. None (Ausencia total)
vacio = None
print(bool(vacio))  # False

print(bool(False)) 
print(bool(True))

