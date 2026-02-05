# Programa: Ejemplo de concatenacion de cadenas

#1. Usando el operador +
nombre = "Lucia"
apellido = "Garcia"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

#2. Usando el metodo print
edad = 28
print("Usando comas:", "nombre:", nombre_completo, ", edad:", edad)

#3. Usando f-strings
ciudad = "barcelona"
pais = "España"
profesion = "ingeniera"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad + 1}, años y soy {profesion} en {ciudad}, {pais}"
print(presentacion)
