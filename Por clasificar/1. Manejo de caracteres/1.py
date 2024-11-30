"""
1. Escribe un programa que lea un carácter del teclado y escriba por pantalla su código o valor dentro
de la tabla ASCII.
"""

# Entrada de datos
caracter = input("Ingrese un caracter: ")
# Proceso
codigo_ascii = ord(caracter)
# Salida
print(f"El código ASCII del caracter '{caracter}' es: {codigo_ascii}")
