"""
Docstring for python de Udemy.5. Entrada de datos.py.46. Ejemplo de cadenas y la funcion
"""

# Error comun de principiante
respuesta_usuario = "False" # Esto es texto

# La funcion bool evalua si el string está vacio
es_verdadera = bool(respuesta_usuario)

print(f"El valor es: {es_verdadera}")
# Output: El valor es: True
# ¿Por qué? Porque el string "false" tiene 5 letras. NO está vacio.

# Forma correcta de valida vacio:
texto_vacio = ""
print(bool(texto_vacio))

