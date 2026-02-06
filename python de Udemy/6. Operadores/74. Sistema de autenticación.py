"""
Docstring for python de Udemy.6. Operadores.75. Sistema de autenticación

Crea un programa para validar el usuario y password proporconados por el usuario.

Crea 2 constantes con lso valores correcos y posteriormente compara que el usuario y passowrd prorporcionados por el usuario sean validos.

Debe solicitar el usuario y el password al usuaio y si son iguales que los valores correctos almacenados en las constante debe imprimir True, de lo contrario debe imprimir False
"""

print("**** INCIIO DE SESION ****")

USUARIO = "admin"
CONTRASEÑA = "123"

usuario = input("Ingresa el usuario: ")
contraseña = input("Ingresa la contraseña: ")

Resultado = (usuario.strip() == USUARIO and contraseña.strip() == CONTRASEÑA)
print(Resultado)