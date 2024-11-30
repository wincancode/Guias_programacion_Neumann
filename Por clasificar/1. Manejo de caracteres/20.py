
"""
20. Resuelva el palíndromo del ejercicio 19 usando ciclo while
"""

# Entrada de datos
texto = input("Ingrese un texto: ")
# Proceso
es_palindromo = True
i = 0
while i < len(texto) // 2:
    if texto[i] != texto[len(texto) - i]:
        es_palindromo = False
        break
    i += 1
# Salida
if es_palindromo:
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")
