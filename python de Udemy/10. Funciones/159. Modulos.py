# ------------ METODO 1 --------------
import modulo_funcion_sumar_159

print("**** Funcion sumar ***")

# Llamar a la funcion
if __name__ == "__main__":
    resultado_funcion = modulo_funcion_sumar_159.sumar(8, 5)
    print(f"Resultado de la funcion {resultado_funcion}")

# ------------ METODO 2 --------------
print()
from modulo_funcion_sumar_159 import sumar

print("**** Funcion sumar ***")

# Llamar a la funcion
if __name__ == "__main__":
    resultado_funcion = sumar(8, 5)
    print(f"Resultado de la funcion {resultado_funcion}")
