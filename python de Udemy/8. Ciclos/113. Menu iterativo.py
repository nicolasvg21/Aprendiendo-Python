print("**** SISTEMA DE ADMINISTRACION DE CUENTAS ****")

salir = False
while not salir:
    print(f""" Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir""")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        print("Creando tu cuenta ...\n")
    elif opcion == 2:
        print("Elinando tu cuenta ...\n")
    elif opcion == 3:
        print("Saliendo del sistema. Hasta pronto!\n")
        salir = True
    else:
        print("Opcion invalida, le doy solo 3 opciones del 1-3 sea serio")
else:
    print("Terminando el sistema de adminsitración de cuentas")
