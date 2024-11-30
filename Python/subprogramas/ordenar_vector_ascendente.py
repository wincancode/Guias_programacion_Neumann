
def ordenar_vector_ascendente(vector):
    for i in range(len(vector)):
        for j in range(i + 1, len(vector)):
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]

# Example usage
if __name__ == "__main__":
    vector = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    ordenar_vector_ascendente(vector)
    print("Vector ordenado:", vector)