
"""
21. Escribe un programa que lea del teclado una lista de valores reales positivos los almacene en un
vector y calcule la media de esta lista.
"""

import numpy as np

# Declaracion de variables
lista_valores = []
suma_valores = 0
media = 0

# Entrada de datos


n = int(input("Ingrese la cantidad de valores: "))

for i in range(n):
    valor = float(input(f"Ingrese el valor {i+1}: "))
    lista_valores.append(valor)

# Proceso
suma_valores = sum(lista_valores)
media = suma_valores / n

# Salida
print(f"La media de los valores ingresados es: {media}")
