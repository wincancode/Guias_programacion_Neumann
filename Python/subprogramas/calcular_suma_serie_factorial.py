
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def calcular_suma_serie_factorial(n):
    suma = 0
    for i in range(1, n + 1):
        factorial = calcular_factorial(i)
        suma += i / factorial
    return suma

# Example usage
if __name__ == "__main__":
    n = 5
    print(f"La suma de la serie factorial hasta {n} es {calcular_suma_serie_factorial(n)}")