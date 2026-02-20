"""
Docstring for python de Udemy.8. Ciclos.114. Reto cajero automatico

Aplicacion cajero automatico

Se les deja crear la aplicacion de cajero automatico

Las funcione sprincipales de un cajero automatico son: depositar, retirar y consultar el saldo.

El saldo puede tener un valor inicial por ejemplo $1.000,00

Si haces un retiro se resta de tu saldo. Y si haces un depósito se suma atu saldo
"""

print("*** Cajero automatico***")

saldo = 1000
transaccion_completada = True
while transaccion_completada:
    print(f"""Opciones:
    1. Consultar salgo
    2. Consignar dinero
    3. Retirar dinero
    4. Salir del panel""")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        print(f"El saldo de tu cuenta es de: ${saldo:.2f}")
        print("Deseas realizar otra operación?\n")

    elif opcion == 2:
        dinero = float(input("Cuanto dinero deseas consignar: $"))
        saldo += dinero
        print(f"\nEl saldo de tu cuenta es de ${saldo:.2f}")
        print("\nDeseas realizar otra operación?\n")
    
    elif opcion == 3:
        dinero = float(input("Cuanto dinero deseas retirar: $"))
        if dinero <= saldo:
            saldo -= dinero
            print(f"\nEl saldo de tu cuenta es de ${saldo:.2f}")
            print("\nDeseas realizar otra operación?\n")
        else:
            print(f"mi elmanazo no te alcanza el cash, tu saldo es de: ${saldo}")
    elif opcion == 4:
        transaccion_completada = False
        print("Has salido exitosamente, vuelve pronto!")
    else:
        print("Vea sapo solo tiene 4 opciones de 1-4, escoja una de esas")
else:
    print("Terminando la aplicacion de cajero automatico")
    