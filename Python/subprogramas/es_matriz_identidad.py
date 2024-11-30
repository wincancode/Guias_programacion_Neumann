
def es_matriz_identidad(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
    return True

# Example usage
if __name__ == "__main__":
    matriz = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    print(f"¿Es la matriz identidad? {es_matriz_identidad(matriz)}")