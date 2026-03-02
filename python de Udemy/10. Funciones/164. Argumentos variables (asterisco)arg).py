print("*** Argumentos variables ***")

def superheroe_superpoderes(superheroe, nombre, *args): # *args siempre debe ir al final de la llamada del método
    print(f"Superherore: {superheroe} - {nombre} - {args}")
    # Iteramos los superpoderes
    for superpoder in args:
        print(f"\tSuperpoder: {superpoder}")

# Llamar la funcion
superheroe_superpoderes("spiderman", "Peter Parker", "Instinto Aracnido", "Telaraña")

# si copiamos la misma linea de codigo pero con el final pero sin los argumentos, este se va a imprimir vacío
superheroe_superpoderes("spiderman", "Peter Parker")

superheroe_superpoderes("Ironman", "Tony Stark", "Millonario", "Playboy", "Filantropo")

# Es opcional enviar argumentos variables
superheroe_superpoderes("Mi vecino", "Juan Perez")
