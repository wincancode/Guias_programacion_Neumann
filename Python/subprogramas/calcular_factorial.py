"""
10. Escriba una función que permita calcular el Factorial de un número n dado por parámetros.
"""

def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Example usage
if __name__ == "__main__":
    n = 5
    print(f"El factorial de {n} es {calcular_factorial(n)}")