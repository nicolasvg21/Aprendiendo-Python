# Ejemplo: Cadenas inmutables

animal = "Gato"

# animal[4] ="s" # provoca un error
# Correcto: Concatenar  (sumar)
# Tomamos "gato" + "s" y lo guardamos en una nueva variable
plural = animal + "s"

print(animal) # Salida "Gato2 (Intacto)
print(plural) # Salida: "Gatos" (nuevo objeto)

plural = f"{animal}s"
print(plural)
