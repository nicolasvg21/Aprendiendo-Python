"""
Docstring for python de Udemy.5. Entrada de datos.py.55. Reto - Generador de emails

Se solicita crea una nueva version del sistema generador de emails.

Para generar un email se debe solicitar

- Nombre -> Ej: Juan Carlos
- Apellido >- Ej: Homez Lara
- Empresa -> Ej: Global mentoring
- Extension de dominio -> Ej: .com.mx

El resultado debe ser:

juan.carlos.gomez.lara@globalmentoring.com.mx
"""
nombres = input("Escribe tu o tus nombres: ")
apellidos = input("\nEscribe tu o tus apellidos: ")
empresa = input("\nEscribe el nombre completo de tu empresa: ")
dominio = input("\nEscribe de forma clara el dominio de tu empresa: ")

nombre_normalizado = nombres.strip().lower().replace(" ", ".")

apellidos_normalizado = apellidos.strip().lower().replace(" ", ".")

empresa_normalizado = empresa.strip().strip().lower().replace(" ","")

dominio_normalizado = dominio.strip().lower().replace(" ","")

print(f""" Hola {nombres}
      El resultado de su generador de emails es:
      {nombre_normalizado}.{apellidos_normalizado}@{empresa_normalizado}{dominio_normalizado})
      Felicidades!!!!!
""")




