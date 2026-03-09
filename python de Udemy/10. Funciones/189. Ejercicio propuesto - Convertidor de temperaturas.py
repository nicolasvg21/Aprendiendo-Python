print("*** Ejercicio: Convertido de tempearatura ***")

#Realizar dos funciones para ocnvertir de celcius a fahrenheit yviceversa

def celcius_fahnernheit(temp_celcius):
    fahrenheit = (temp_celcius * 1.8) + 32
    return fahrenheit

def fahrenheit_calcius(temp_fahrenheit):
    celcius = (temp_fahrenheit-32)/1.8
    return celcius

if __name__=="__main__":
    while True:
        print("""\nCalculadora de temperaturas
        1.Pasar de C° a F°
        2.Pasar de F° a C°
        3.salir""")
        opcion = int(input("Escoje una opcion: "))
        if opcion == 1:
            temp_celcius = float(input("\nIngresa la temperatura en celcius: "))
            print(f"El resultado de la conversion de {temp_celcius}°C a °F es: {celcius_fahnernheit(temp_celcius)}°F")

        elif opcion == 2:
            temp_fahrenheti = float(input("\nIngresa la temperatura en fahrenheit: "))
            print(f"El resultado de la conversion de {temp_fahrenheti}°F a °C es: {fahrenheit_calcius(temp_fahrenheti)}°C")
        
        elif opcion == 3: 
            print("saliste con exito!")
            break
        else:
            print("Intente otra vez maldita sea son solo 3 opciones")

        