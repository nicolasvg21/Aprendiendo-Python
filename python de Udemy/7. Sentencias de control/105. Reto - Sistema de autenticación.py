"""
Docstring for python de Udemy.7. Sentencias de control.105. Reto - Sistema de autenticación

sistema de autenticacion

Crear un sitema para validad los valores de usuario y password proporcionados.

Se deben definir dos constantes con los valores validos de usuario y password

Y el sistema debe comparar los valores validos contra los valores proporcionados

Se deben considerar 4 casos:

1. Usuario y password validos. Debe imprimir: Bienvenidos al sistema"
2. Usuario invalido
3. Password invalido
4. Usuario y password invalidos
"""
USUARIO_VALIDO = "admin"
CONTRASENA_VALIDA = "1234"


usuario = input("Ingresa tu usuario: ")
contraseña = input("Ingresa tu contraseña: ")


if usuario == USUARIO_VALIDO and contraseña == CONTRASENA_VALIDA:
    print("Bienvendio al sistema")
elif usuario == USUARIO_VALIDO and contraseña != CONTRASENA_VALIDA:
    print("Su contraseña es invalida")
elif usuario != USUARIO_VALIDO and contraseña == CONTRASENA_VALIDA:
    print("Su usuario es invalido")
else:
    print("Su usario y contraseña son invalidos")
