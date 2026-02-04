"""
Docstring for python de Udemy.5. Entrada de datos.py.49. Ejemplo sistema de empleados

Sistema de empleados

Crea un programa para soolicitar la infomacion de un empleado, introduciendo los datos por consola

- Nombre empleaod
- Edad del empleado (convertir a entero)
- Salario del empleado (convertir a flotante)
- Es jefe de departamenteo) (si/no)
"""

print("**** SISTEMA DE EMPLEAODS ****")

nombre_empleado = input("\nNombre del empleado: ")
edad_empleado = int(input("Edad del empleado: "))
salario_empleado = float(input("salario del empleado: "))
es_jefe_departamento = input("Es jefe de departamento (Si/No) ")

# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si"

# Imprimir los valores del empleado
print("\nDatos del empleado")
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salario: ${salario_empleado:.2f}")
print(f"Es jefe de departamento? {es_jefe_departamento}")



