
# Construya un algoritmo utilizando estructuras iterativas que calculen el factorial de
# un número entero positivo n. La función factorial, representada por n!, es ampliamente
# utilizada, y se especifica que n!= n*(n-1)!, y además 0!=1.

n = int(input("Ingrese un número entero positivo: "))

if n < 0:
    print("El número ingresado no es positivo.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es {factorial}.")