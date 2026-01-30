print("6.2 EXCEPCIONES PERSONALIZADAS")
print("Ademas de las ecepciones incoroporadas en python, tambien puedes crear tus propies ecepciones pesonalizadas. Esto es util cuando deseas manear situalciones especificas de tu programa.")
print("")
print("Para crear una excepcion personalizada, debes crear una clase que herede de la clase base Exceoction ode una de sus subclases")
print("")

def funcion():
    # Codigo que puede generar una excepcion personalizada
    if condicion:
        raise Exception("Descripcion del error")

try:
    funcion()
except Exception as e:
    print(f"error: {str(e)}")

print("")

print("En este ejemplo, se define una funcion llamada funcion. Dentro de la funcion, se verifica una condicion y, si se cumple, se genera una excepcion utilizando la declaracion raise. En lugar de crear una clase personalizadam seutiliza directamente la clase base")

print("")

print("Luego, se utiliza un blouqe try-except para capturar y manejar la excepcion. La variable e se tuliza para acceder a la descripcion del error proporcionada al generar la excepcion.")
print("")
print("El manejo de errores y ecepciones es una parte fundamental de la programacion en pyhton. Te permite manejar situaciones inesperadas de manejar controlada y evitar que tu programa se bloqueee o detenga abruptamente.")
print("")
print("Cuando ocurre un error en tu codigo, Python genera un aexcepcion. Al utilizar blques try-except, puedes captuar y manejar estas ecepciones de manejara adecuada. Puedes especificar diferentes bloques except apra manejar distintos tipos de excepciones y realizar acciones en cada caso")
print("Ademas, el bloque finally te permite ejecutar codifo de limpieza o liberaciond recursos. independiente mente de si ocurrio una excepcion o no. Esto e sutil ara garantizar que ciertas acciones se realicen siempre, como cerrar archivos o conexiones de la base de datos.")
print("")
print("IMPORTANTE")
print("Considera los posibles errores que pueden ocurrir en tu código y utiliza el manejo de excepciones adecuado para manejarlos de manera apropiada. Esto hará que tus programas sean más robustos y confiables.")