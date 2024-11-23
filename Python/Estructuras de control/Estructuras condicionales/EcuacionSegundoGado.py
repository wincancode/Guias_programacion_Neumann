#3 Diseñar un algoritmo para resolver una ecuación de segundo grado.

# Entradas
print("Ecuación de segundo grado")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Procesos
if a == 0:
    if b == 0:
        if c == 0:
            solucion = "Infinitas soluciones"
        else:
            solucion = "No tiene solución"
    else:
        solucion = -c / b
else:
    discriminante = b ** 2 - 4 * a * c
    if discriminante < 0:
        solucion = "No tiene solución"
    elif discriminante == 0:
        solucion = -b / (2 * a)
    else:
        solucion1 = (-b + discriminante ** 0.5) / (2 * a)
        solucion2 = (-b - discriminante ** 0.5) / (2 * a)
        solucion = (solucion1, solucion2)

# Salidas
print(f"La solución de la ecuación {a}x^2 + {b}x + {c} = 0 es: {solucion}")
