"""
8. Elabore un programa que verifique si un caracter ingresado desde el teclado es, o no es, una letra.
"""

# Entrada de datos
caracter = input("Ingrese un caracter: ")
# Proceso y salida
if caracter.isalpha():
    print(f"El caracter '{caracter}' es una letra.")
else:
    print(f"El caracter '{caracter}' no es una letra.")
