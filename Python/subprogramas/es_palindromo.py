
def es_palindromo(string):
    return string == string[::-1]

# Example usage
if __name__ == "__main__":
    string = "radar"
    print(f"¿Es '{string}' un palíndromo? {es_palindromo(string)}")