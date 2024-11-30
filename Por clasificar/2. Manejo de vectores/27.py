"""
27. Elabore un programa que escriba el promedio de los elementos que se encuentran en las
posiciones pares y el promedio de los elementos de los elementos que se encuentran en las
posiciones impares de un vector que contiene valore enteros.

que hay que hallar:

- el promedio de los elementos en posiciones pares
    - cantidad de elementos pos pares
    - suma de pos pares
- el promedio de los elementos en las posiciones impares
    - cantidad de elementos en pos impares
    - soma de pos impares
"""

# region Declaracion de variables
vector = [5, 10, 3, 8, 2]

promedio_pares = 0
promedio_impares = 0

# contadores
cantidad_pares = 0
cantidad_impares = 0

# acumuladores
suma_pares = 0
suma_impares = 0

# endregion

# Proceso

for i in range(0, len(vector)):
    if i % 2 == 0:
        # Entonces es par
        suma_pares = suma_pares + vector[i]
        cantidad_pares = cantidad_pares + 1
    else:
        # Entonces es impar
        suma_impares = suma_impares + vector[i]
        cantidad_impares = cantidad_impares + 1

promedio_pares = suma_pares / cantidad_pares
promedio_impares = suma_impares / cantidad_impares

print("Promedio pares: ", promedio_pares,
      "; promedio impares: ", promedio_impares)
