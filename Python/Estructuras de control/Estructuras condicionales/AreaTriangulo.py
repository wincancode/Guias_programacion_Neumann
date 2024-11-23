
# . Diseñar un algoritmo que calcule el área de un triangulo en función de las
# longitudes de sus lados.
# Area = sqrt(s * (s - a) * (s - b) * (s - c)), donde s = (a + b + c) / 2 y a, b y c son los lados del triángulo.

# Entradas
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

# Procesos
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Salidas
print(f"El área del triángulo con lados de longitud {a}, {b} y {c} es: {area}")