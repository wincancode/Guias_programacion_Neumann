
"""
16. Diseñe un programa que convierta a mayúsculas todas las vocales contenidas en un string.
"""

# Entrada de datos
texto = input("Ingrese un texto: ")
# Proceso
texto_aMayus = texto.replace("a", "A")
texto_eMayus = texto_aMayus.replace("e", "E")
texto_iMayus = texto_eMayus.replace("i", "I")
texto_oMayus = texto_iMayus.replace("o", "O")
texto_mayusculas = texto_oMayus.replace("u", "U")

# Salida
print(f"El texto con todas las vocales en mayúsculas es: {texto_mayusculas}")
