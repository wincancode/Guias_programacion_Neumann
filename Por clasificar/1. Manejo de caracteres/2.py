
"""
2. Elabore un programa que lea un valor tipo byte desde el teclado y escriba por pantalla el carácter
correspondiente dentro de la tabla ASCII.
"""

# Entrada de datos
valor_byte = int(input("Ingrese un valor tipo byte: "))
# Proceso
caracter_ascii = chr(valor_byte)
# Salida
print(f"El caracter correspondiente al valor {valor_byte} en la tabla ASCII es: {caracter_ascii}")

