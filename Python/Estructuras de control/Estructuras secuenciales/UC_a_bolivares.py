"""
1. Escriba un programa que calcule y escriba el valor en bolívares de una cantidad dada de
unidades tributarias (1 U.T. =1.500,00).
"""



# Declaracion de variables
valor_ut = 1500
cantidad_ut = 0
valor_bolivares = 0

# Entrada de datos
cantidad_ut = int(input("Ingrese la cantidad de unidades tributarias: "))
# Proceso
valor_bolivares = valor_ut * cantidad_ut
# Salida
print(f"El valor en bolivares de {cantidad_ut} unidades tributarias es: {valor_bolivares}")
