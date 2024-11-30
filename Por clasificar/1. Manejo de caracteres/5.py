"""
5. Realice un programa que lea un carácter del teclado y escriba en pantalla el carácter que le precede
en el código ASCII.
"""

# Entrada de datos
caracter = input("Ingrese un caracter: ")
# Proceso
caracter_anterior = chr(ord(caracter) - 1)
# Salida
print(f"El caracter anterior a '{caracter}' en la tabla ASCII es: {caracter_anterior}")

