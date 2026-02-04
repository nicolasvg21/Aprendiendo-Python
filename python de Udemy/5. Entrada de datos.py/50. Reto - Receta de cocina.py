"""
Docstring for python de Udemy.5. Entrada de datos.py.50. Reto - Receta de cocina

Crear un programa para solicitar algunos valores importantes para una receta de cocina

Los valores que debe introducri el usuario son:

- Nombre de la receta
- Ingredientes
- Tiempo
- Dificultad ("Facil, media, alta")
"""

print("**** RECETA DE COCINA ****")

nombre_receta = input("\nCual es el nombre de la receta: ")
ingredientes = input("Hazme la lista de los ingredientes: ")
tiempo = int(input ("Cuantos minutos dura la receta: "))
dificultad = input("Que tan dificil (facil, medio o dificil): ")
print("\n------------------------------------")
print(f"\nel nombre de la receta es: {nombre_receta}")
print(f"los ingredintes de la receta son: {ingredientes}")
print(f"El tiempo que se tarda es: {tiempo}")
print(f"la dificultad es: {dificultad}")


