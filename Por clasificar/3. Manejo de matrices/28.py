"""
28. Dada una matriz inicializada en el código del programa, haga un recorrido por filas para
imprimirla en pantalla. Utilice la matriz:
matriz = np.array([[9, 4, 5], [0, 3, 7], [8, 1, 2]])
"""

import numpy as np


matriz = np.array([[9, 4, 5], [0, 3, 7], [8, 1, 2]])

for fila in matriz:
    print(fila)
