# Programa: Aplicar el concepto de slicing

texto = "PROGRAMACION"

# 1. Basico [inicio:fin]
print(texto[0:4]) # "PROG"

# 2. Atajo desde el inicio [:fin]
print(texto[:4]) # PROG" (Asume inicio 0)

# 3. Atajo hasta el final[inicio:]
print(texto[8:]) # "CION" (Hasta el ultimo caracter)

# 4.[Indices negativos]
print(texto[-4:]) #"CION" (Los ultimo 4 caracteres)

# 5. Pasos [::paso] (invertir cadena)
print(texto[::2]) # #OINCAMARGORP"

print(texto[2:4])