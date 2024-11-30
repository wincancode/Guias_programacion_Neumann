
#include <iostream>
#include <string>

int convertir_a_decimal(const std::string& binario) {
    int decimal = 0;
    for (size_t i = 0; i < binario.size(); ++i) {
        decimal += (binario[i] - '0') * (1 << (binario.size() - i - 1));
    }
    return decimal;
}

int main() {
    std::string binario = "1010";
    std::cout << "El binario " << binario << " en decimal es " << convertir_a_decimal(binario) << std::endl;
    return 0;
}