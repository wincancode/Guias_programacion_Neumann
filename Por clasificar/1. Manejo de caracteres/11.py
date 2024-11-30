"""
11. Diseñe un programa que lea un carácter desde el teclado y si es una letra minúscula la convierta
a mayúscula. Nota: no utilice métodos incorporados de Python.
"""

# Entrada de datos
caracter = input("Ingrese un caracter: ")
# Proceso y salida
if caracter.islower():
    caracter_mayuscula = chr(ord(caracter) - 32)
    print(f"El caracter '{caracter}' convertido a mayúscula es: {caracter_mayuscula}")
else:
    print(f"El caracter '{caracter}' no es una letra minúscula.")
