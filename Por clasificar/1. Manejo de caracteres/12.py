"""
12. Diseñe un programa que lea un carácter desde el teclado y si es una letra minúscula la convierta
a mayúscula usando métodos incorporados de Python.
"""

# Entrada de datos
caracter = input("Ingrese un caracter: ")
# Proceso y salida

if caracter.isalpha():
    caracter_mayuscula = caracter.upper()
    print(f"El caracter '{caracter}' convertido a mayúscula es: {
          caracter_mayuscula}")
else:
    print("el caracter no es una letra")
