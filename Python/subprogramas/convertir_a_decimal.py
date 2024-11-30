
def convertir_a_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * (2 ** (len(binario) - i - 1))
    return decimal

# Example usage
if __name__ == "__main__":
    binario = "1010"
    print(f"El binario {binario} en decimal es {convertir_a_decimal(binario)}")