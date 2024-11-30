

"""
29. Dada una matriz inicializada en el código del programa, haga un recorrido por columnas para
imprimirla en pantalla. Utilice la matriz:
matriz = np.array([[9, 4, 5], [0, 3, 7], [8, 1, 2]])
"""

import numpy as np

matriz = np.array([[9, 4, 5], [0, 3, 7], [8, 1, 2]])

for columna in matriz.T:
    print(columna)

