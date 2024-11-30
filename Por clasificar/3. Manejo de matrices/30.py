

"""
30. Escriba un programa que llene una matriz cuadrada con datos tipo entero capturados desde el
teclado, realice un recorrido por filas.
"""

import numpy as np

n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

matriz = np.zeros((n, n), dtype=int)

print("va a ingresar ", n*n, " elementos")

for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Ingrese el elemento [{i}][{j}]: "))

for fila in matriz:
    print(fila)
