"""
4. Diseñe un programa que lea un carácter del teclado y escriba en pantalla el carácter que le sigue
en el código ASCII.
"""

# Entrada de datos
caracter = input("Ingrese un caracter: ")
# Proceso
siguiente_caracter = chr(ord(caracter) + 1)
# Salida
print(f"El caracter siguiente a '{caracter}' en la tabla ASCII es: {siguiente_caracter}")
