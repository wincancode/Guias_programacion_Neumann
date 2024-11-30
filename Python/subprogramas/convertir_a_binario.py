
def convertir_a_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

# Example usage
if __name__ == "__main__":
    numero = 10
    print(f"El número {numero} en binario es {convertir_a_binario(numero)}")