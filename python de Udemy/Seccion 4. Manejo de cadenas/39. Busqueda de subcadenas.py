"""
Docstring for python de Udemy.Seccion 4. Manejo de cadenas.39. Busqueda de subcadenas

Buscar subcadenas (find): El método find() devuelve el indice de la primera aparicion de la subcadena. Si no encuentra la subcadena, devuelve -1
"""

cadena = "Hola, mundo!"
indice = cadena.find("mundo")

print(f"indice de la subcadena mundo: {indice}") # Imprime 6

# Obtener el indice de la subcadena de hola
indice = cadena.find("Hola")
print(f"Indice de la subcadena de Hola {indice}")

