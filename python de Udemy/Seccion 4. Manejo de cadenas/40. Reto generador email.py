#POR ULTIMO UN DATO QUE ESTE HPTA NO FUE CAPAZ DE TIRAR, EN NINGUN VIDEO ES QUE EL COMANDO texto.strip() sirve para quitar espacios al inicio y al final de la cadena en la cadena

nombre = " Nicolas Vargas Gamboa "
nombre_sin_spaces = nombre.strip()
print(nombre_sin_spaces)


"""
Docstring for python de Udemy.Seccion 4. Manejo de cadenas.40. Reto generador email

Crea un programa para genera un email a partir de los siguientes datos:

Nombre: Ubaldo Acosta Soto
Empresa: Global Mentoring
Dominio: com.mx

Resultado final:

email: ubaldo.acosta.soto@globalmentoring.com.mx
"""

primer_nombre = "Ubaldo"
primer_apellido = "Acosta"
segundo_apellido = "Soto"
empresa = "Global mentoring"
dominio = ".com.mx"

nombre_completo = primer_nombre + " " + primer_apellido + " " + segundo_apellido

primer_nombre_normalizado = primer_nombre.lower()
primer_apellido_normalizado = primer_apellido.lower()
segundo_apellido_normalizado = segundo_apellido.lower()
nombre_total_normalizado = primer_nombre_normalizado+ "." + primer_apellido_normalizado + "." + segundo_apellido_normalizado

nEmpresaN = empresa.lower()
print(nEmpresaN)

print()
print("*** GENERADOR DE EMAIL ***")
print("Nombre de usuario:", nombre_completo)
print("Nombre de usuario normalizado:", nombre_total_normalizado)
print()
print("Nombre de la empresa:", empresa)
print("Extension del dominio:", dominio)
print()
print("Email final generado: " + nombre_total_normalizado + "@" + nEmpresaN[0:6] + nEmpresaN[7:16] + dominio)

print()

print("------------------------------------------------------------")
print("-" * 60)

print()

print("ahora si sigue la explicacion del profesor")
print()
#Generador de emails
print("*** GENERADOR DE EMAIL ***")
print()

# Nombre completo del usuario
nombre_completo = "Ubaldo Acosta Soto "
print(f"Nombre de usuario:{nombre_completo}")

# Procesar o normalizar el nombre del usuario
# Limpiamos los espcios en blanco al inicio y al final
nombre_normalizado = nombre_completo.strip().replace(" ", ".")

# Convertimos a minusculas
nombre_normalizado = nombre_normalizado.lower()
print(f"Noombre usuario normalizado: { nombre_normalizado}")
print()

# Datos de la empresa
nombre_empresa = " Global Mentoring "
print(f"Nombre de la empresa: {nombre_empresa}")
extension_dominio = ".com.mx "
print(f"extension del domino: {extension_dominio}")
print() 

# quitamos los espacios en blanco pegando las palabras y convertimos a mayusculas
nombre_empresa_normalizado = nombre_empresa.replace(" ", "").lower()
dominio_email_normalizado = f"@{nombre_empresa_normalizado}{extension_dominio}"
print(f"Dominio del email normalizado: {dominio_email_normalizado}")
print()

#Creamos el email final
email = f"{nombre_normalizado}{dominio_email_normalizado}"
print(f"Email final generado: {email}")

#Ojito a esta jugada

nombre = "Python"
print(nombre.lower().replace("p","J"))

# como la funcion lower volvio todas las letras en minuscula, pues al haber hecho esa accion antes del replace pues python permite hacer el reemplazo 