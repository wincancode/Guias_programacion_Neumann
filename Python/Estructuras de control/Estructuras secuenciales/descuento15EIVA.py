
"""
4. Una tienda ofrece un descuento de 15% sobre el monto de compra para sus clientes, elabore
un programa que calcule el porcentaje de descuento de esa compra, el monto a pagar por el
IVA (16% de IVA) y finalmente el total a pagar
"""

# Declaracion de variables
monto_compra = 0
descuento = 0
monto_iva = 0
total_pagar = 0

# Entrada de datos
monto_compra = float(input("Ingrese el monto de compra: "))
# Proceso
descuento = monto_compra * 0.15
monto_iva = monto_compra * 0.16
total_pagar = monto_compra - descuento + monto_iva
# Salida
print(f"El porcentaje de descuento de la compra es: {descuento}")
print(f"El monto a pagar por el IVA es: {monto_iva}")
print(f"El total a pagar es: {total_pagar}")

