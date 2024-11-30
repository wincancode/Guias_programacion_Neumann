

"""
32. Dadas dos matrices cuadradas, cambie la diagonal principal por la primera fila.

M1
[1,2,3]
[4,5,6]
[7,8,9]

M2
[10,11,12]
[13,14,15]
[16,17,18]

M3
[10,2,3]
[4,11,6]
[7,8,12]


1. importar numpy
2. pedir tamaño de las matrices
3. crear las matrices nxn

4. llenar las matrices

5. Cambiar la diagonal principal de M1 por la primera fila de M2
"""


import numpy as np

n = int(input("Ingrese el tamaño de las matrices: "))

m1 = np.zeros((n, n), dtype=int)
m2 = np.zeros((n, n), dtype=int)


for i in range(n):
    for j in range(n):
        m1[i, j] = int(input(f"Ingrese el valor [{i}, {j}] de la matriz 1: "))

for i in range(n):
    for j in range(n):
        m2[i, j] = int(input(f"Ingrese el valor [{i},{j}] de la matriz 2: "))

# 5. Cambiar la diagonal principal de M1 por la primera fila de M2

"""

M1
[1,2,3]
[4,5,6]
[7,8,9]

M2
[10,11,12]
[13,14,15]
[16,17,18]

M3
[10,2,3]
[4,11,6]
[7,8,12]


M1        M2
[0,0] = [0,0]
[1,1] = [0,1]
[2,2] = [0,2]
[3,3] = [0,3]
[4,4] = [0,4]
[5,5] = [0,5]

...

[n,n] = [0,n]




"""

for i in range(n):
    m1[i, i] = m2[0, i]
    print(f"[{i},{i}] = [0,{i}]")

for valor in m1:
    print(valor)
