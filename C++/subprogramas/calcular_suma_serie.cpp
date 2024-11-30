
#include <iostream>

double calcular_suma_serie(int n) {
    double suma = 0;
    for (int i = 0; i < n; ++i) {
        suma += 1.0 / (1 << i);
    }
    return suma;
}

int main() {
    int n = 5;
    std::cout << "La suma de la serie hasta " << n << " es " << calcular_suma_serie(n) << std::endl;
    return 0;
}