"""
Docstring for python de Udemy.8. Ciclos.118. Popuesto - Creacion de passwaord

Creacion y validacion de password

Crear un programa para solicitar la validacion al moemnto de crear un valor de un password o contraseña.

La contraseña debe tener al menos 6 caracteres.

En caso de no cumplir con esta condicion el programa debe volver a solicitar un nuevo valor hasta que cumpla con la condicion 

Si el valor proporcionado es valido, se debe imprimir: "Password Valido" y debe terminar la ejecucion del sistema
"""

print("*** Creacion y validadcion de contraseña ***")

password = True
while password:
    contraseña = input("\nPor favor ingresa una nueva contraseña para tu cuenta con minimo 6 caracteres: ")
    caracteres = len(contraseña)
    if caracteres >= 6:
        print("\nSu contraseña cumple con los requisitos para su generación, contraseña creada")
        password = False
        print("Continue en la siguiente pagina")
    else:
        print("\nMaldita sea son solamente mas de 6 caracteres, tráteme serio me vale verga sin son mayusculas minusculas signos o numeros")
else:
    print("\nSecuencia while ha acabado")

print("**** MI PROFE LO HARÍA ASÍ ****")

password = input("Ingresa un passward (debe tener almenos 6 caracteres: ")

# Validar el password
while len(password) <6:
    print("\nEl password no cumple con los requisitos. Debe tener al menso 6 caracteres")
    password = input("Ingresa un nuevo valor de password: ")
else:
    print("El valor depassword es valido")