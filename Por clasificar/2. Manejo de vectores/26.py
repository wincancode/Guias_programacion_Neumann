

"""
26. Escriba un programa que determine si un elemento esta contenido dentro de un vector, el
programa debe utilizar valores booleanos, si encuentra el elemento solo debe decir en cual
posición del vector fue encontrado.
"""

# Declaracion de variables
vector = [5, 10, 3, 8, 2]
elemento = 8
encontrado = False
posicion = 0
# Proceso

for i in range(len(vector)):
    if vector[i] == elemento:
        encontrado = True
        posicion = i

if encontrado:
    print("encontrado en la posicion ", posicion)
else:
    print("Elemento no se encuentra en el vector")

# Salida
