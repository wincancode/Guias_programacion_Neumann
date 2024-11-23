
# . Tres numero naturales A, B y C forman una terna pitagórica cuando se cumple la
# relación A2 + B2 = C2
# . Escriba un algoritmo que leídos tres números diga si forman una
# terna pitagórica

# Entradas
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

# Procesos
if a ** 2 + b ** 2 == c ** 2:
    resultado = "forman"
else:
    resultado = "no forman"

# Salidas
print(f"Los números {a}, {b} y {c} {resultado} una terna pitagórica")