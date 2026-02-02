import math

print('*** Constantes en python')

PI = 3.14159
print('El valor de PI es:', PI)

NOMBRE_BASE_DATOS = 'Clientes_db'
print("Nombre de la base de datos:", NOMBRE_BASE_DATOS)

# Esto no se debe hacer, no se debe modificar el valor de una constante
NOMBRE_BASE_DATOS = "Listado clientes db"
print("No cambiar el valor de una constante:", NOMBRE_BASE_DATOS)

# Usar una constante del lenguage pytgon, aunque ne este caso no esta en mayuscula
print("Valor de math.pi", math.pi)


