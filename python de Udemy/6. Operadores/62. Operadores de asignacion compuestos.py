print("**** Operadores de asignacion compuestos ****")

a, b = 10, 15

print(f"\nvalor inicial de a: {a}, b = {b}")

# Operador compuesto de suma +=
a += b      # a += a + b
print(f"\nOperador a += b es: {a}")

# Operador compues de resta -=
a = 10 # reiniciamos la variable a
a -= b # a = a - b
print(f"\nOperador a -= b es: {a}")

# Operador compuesto de multiplicacion *=
a = 10 # reiniciamos la variable a
a *= b 
print(f"\nOperador a *= b es: {a}")

# Operador compuesto de divisiion /=
a = 10 # reiniciamos el valor de a
a /= b # a = a / b
print(f"\nOperador a /= b es: {a:.2f}")

#----------------------------------------------------------------------------

# Tenemos una cadena con nombre y apellido separados por espacio
datos_usuario = "Juan Perez Gonzales"
 
# Usamos split() para dividir la cadena donde haya un espacio
# Y aplicamos asignación múltiple a las variables nombre y apellido
nombre, apellido1, apellido2 = datos_usuario.split()
 
print(f"Nombre: {nombre}")
print(f"Apellido1 : {apellido1}")
print(f"apellido 2: {apellido2}")

# Si la cadena tuviera comas (ej. "Juan,Perez"), usarías datos_usuario.split(',').