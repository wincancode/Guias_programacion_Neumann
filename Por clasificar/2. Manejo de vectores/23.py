
"""
23. Diseñe un programa que recorra un vector y determine el mínimo valor que contiene.
"""

# Declaracion de variables
vector = [100, 10, 3, 8, 2]
minimo = vector[0]

# Proceso
for valor in vector:
    if valor < minimo:
        minimo = valor

# Salida
print(f"El mínimo valor del vector es: {minimo}")

