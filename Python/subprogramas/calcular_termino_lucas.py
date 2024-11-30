
def calcular_termino_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        termino_anterior = 2
        termino_actual = 1
        for i in range(2, n + 1):
            termino_siguiente = termino_anterior + termino_actual
            termino_anterior = termino_actual
            termino_actual = termino_siguiente
        return termino_actual

# Example usage
if __name__ == "__main__":
    n = 6
    print(f"El término {n}-ésimo de la secuencia de Lucas es {calcular_termino_lucas(n)}")