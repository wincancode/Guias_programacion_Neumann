
def encontrar_menor_valor(vector):
    menor_valor = vector[0]
    posicion_menor_valor = 0
    for i in range(1, len(vector)):
        if vector[i] < menor_valor:
            menor_valor = vector[i]
            posicion_menor_valor = i
    print("El menor valor es", menor_valor, "y se encuentra en la posición", posicion_menor_valor)

# Example usage
if __name__ == "__main__":
    vector = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    encontrar_menor_valor(vector)