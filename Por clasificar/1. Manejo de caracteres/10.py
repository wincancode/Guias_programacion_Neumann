"""
10. Elabore un programa que lea un carácter desde el teclado y determine si es o no, un digito.
"""

# Entrada de datos
caracter = input("Ingrese un caracter: ")
# Proceso y salida
if caracter.isdigit():
    print(f"El caracter '{caracter}' es un dígito.")
else:
    print(f"El caracter '{caracter}' no es un dígito.")
