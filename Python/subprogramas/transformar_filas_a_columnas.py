
def transformar_filas_a_columnas(matriz_inicial):
    matriz_final = []
    for j in range(len(matriz_inicial[0])):
        columna = []
        for i in range(len(matriz_inicial)):
            columna.append(matriz_inicial[i][j])
        matriz_final.append(columna)

    print("Matriz Inicial:")
    for fila in matriz_inicial:
        print(fila)

    print("Matriz Final:")
    for fila in matriz_final:
        print(fila)

# Example usage
if __name__ == "__main__":
    matriz_inicial = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    transformar_filas_a_columnas(matriz_inicial)