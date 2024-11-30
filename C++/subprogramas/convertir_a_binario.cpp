
#include <iostream>
#include <string>

std::string convertir_a_binario(int numero) {
    if (numero == 0) {
        return "0";
    }
    std::string binario;
    while (numero > 0) {
        binario = std::to_string(numero % 2) + binario;
        numero /= 2;
    }
    return binario;
}

int main() {
    int numero = 10;
    std::cout << "El número " << numero << " en binario es " << convertir_a_binario(numero) << std::endl;
    return 0;
}