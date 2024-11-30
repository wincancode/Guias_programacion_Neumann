
"""
19. Utilizando valores booleanos elabore un programa que permita determinar si un texto contenido
en una variable tipo string es palíndromo. Debe utilizar funciones para manipulación de cadenas
para determinar el tamaño de la cadena de caracteres contenida en el string. Utilice un ciclo for.
"""


# Entrada de datos
texto = input("Ingrese un texto: ")

# Proceso

#  aeiouuoiea

# 0 - 10-0 = 0 - 10
# 1 - 10-1 = 1 - 9
# 2 - 10-2 = 2 - 8
# ...
# 5 - 10-5 = 5 - 

es_palindromo = True
for i in range(len(texto) // 2):
    if texto[i] != texto[len(texto) - i]:
        es_palindromo = False
        break


# Salida
if es_palindromo:
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")
