"""
Ejercicio: Calculadora de impuestos
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.

Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

print("*** Calculadora de impuestos ***")

def impuestos():
    pago_sin_impuesto = float(input("\nProporciones el pago sin impuesto: "))
    impuesto = float(input("Proporcione el porcentaje del impuesto: "))
    pago_total = pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
    return pago_total

print(f"Pago con impuesto: {impuestos()}")


print("Así lo hace mi profe") #es mejor porque:
# Explícito: Se ve claramente qué necesita la función.
# Reutilizable: Puedes llamarla con cualquier valor.
# Sin efectos secundarios: No depende del estado global.
# Más legible: La interfaz de la función está clara.

def impuestos(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
    return pago_total

pago_sin_impuesto = float(input("\nProporciones el pago sin impuesto: "))
impuesto = float(input("Proporcione el porcentaje del impuesto: "))
pago_con_impuesto = impuestos(pago_sin_impuesto, impuesto)
print(f"Pago con impuesto: {pago_con_impuesto}")
