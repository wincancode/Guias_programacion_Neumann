
"""
31. Recorra una matriz cuadrada por columnas y calcule el promedio de todos los elementos que
contiene.
"""

import numpy as np

n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

matriz = np.zeros((n, n), dtype=int)

# variables

suma_elementos = 0
cantidad_elementos = n*n

for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        suma_elementos = suma_elementos + matriz[i, j]

promedio = suma_elementos / cantidad_elementos

print(f"El promedio de cada columna es: {promedio}")
