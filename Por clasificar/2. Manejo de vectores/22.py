
"""
22. Diseñe un programa que recorra un vector y determine el máximo valor que contiene.
"""

# Declaracion de variables
vector = [5, 10, 3, 8, 2]
maximo = vector[0]

# Proceso

# usando un for each
for valor in vector:  # valor = 5, 10, 3, 8, 2
    if valor > maximo:
        maximo = valor

# usando un for normal
for i in range(len(vector)):
    if vector[i] > maximo:
        maximo = vector[i]

# Salida
print(f"El máximo valor del vector es: {maximo}")
