"""
9. Diseñe un programa que verifique si un caracter ingresado desde el teclado es:
una letra mayúscula, una letra minúscula, o si, no es una letra.
"""

# Entrada de datos
caracter = input("Ingrese un caracter: ")
# Proceso y salida
if caracter.isupper():
    print(f"El caracter '{caracter}' es una letra mayúscula.")
elif caracter.islower():
    print(f"El caracter '{caracter}' es una letra minúscula.")
else:
    print(f"El caracter '{caracter}' no es una letra.")
