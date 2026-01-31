print("7.1 LECTURA Y ESCRITRURA DE ARCHIVOS")
print("Python nos permite leer y escribir datos en archivos externos. Podemos abrir archivos en diferentes modos, como lectura (\"r\"), escritura (\"w\") o anexar (\"a\"), y realizar operaciones de lectura y escritura.")

print("")

print("LECTURA DE ARCHIVOS")
print("Para leer el contenido de un archivo, primero debemos abrirlo utilizando la función open() en modo de lectura ("r"). Luego, podemos leer el contenido del archivo utilizando métodos como read() o readlines().")

print("")

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close() 

print("En este ejemplo, se abre el archivo \"datos.txt\" en modo de lectura utilizando open(). Luego, se lee todo el contenido del archivo utilizando el método read() y se almacena en la variable contenido. Finalmente, se muestra el contenido en la pantalla y se cierra el archivo utilizando el método close().")

print("ESCRITURA DE ARCHIVOS")
print("Para escribir datos en un archivo, lo abrimos en modo de escritura (\"w\") utilizando la función open(). Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá.")

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

print("En este ejemplo, se abre el archivo \"datos.txt\" en modo de escritura utilizando open(). Luego, se escribe la cadena \"¡Hola, mundo!\" en el archivo utilizando el método write(). Finalmente, se cierra el archivo utilizando el método close().")

print("")

print("IMPORTANTE")
print("Es importante cerrar siempre los archivos despue de utilizarlos para liberar los recursos del sistema")

print("")

print("Tambien puedes utilizar la declaracion with para manejar la apertura y cierre de archivos de manera automatica")

print("")

with open("datostxt", "r") as archivo:
    conteido = archivo.read()
    print(contenido)

print("")

print("En este caso, el archivo se abre utilizando la declaracion with y se cierra automaticamente una vez que se sale del bloque with, incluso si ocurre una excepcion.")

print("")

print("La entrada y salida de datos en Python nos brinda una gran flexibilidad para interactuar con el usuario y manipular archivos externos. Podemos solicitar información al usuario, mostrar resultados en la pantalla y leer o escribir datos en archivos de texto. Recuerda siempre manejar adecuadamente la apertura y cierre de archivos, y considerar las posibles excepciones que pueden ocurrir durante las operaciones de entrada/salida.")
