
# Realizar un algoritmo que permita intercambiar entre si los valores de dos
# variables A y B.

# Entradas
a = float(input("Ingrese el valor de la variable A: "))
b = float(input("Ingrese el valor de la variable B: "))

# Procesos
temp = a
a = b
b = temp

# Salidas
print(f"El valor de A es: {a}")
print(f"El valor de B es: {b}")