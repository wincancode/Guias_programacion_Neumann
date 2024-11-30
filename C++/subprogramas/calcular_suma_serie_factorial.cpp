
#include <iostream>

int calcular_factorial(int n) {
    int factorial = 1;
    for (int i = 1; i <= n; ++i) {
        factorial *= i;
    }
    return factorial;
}

double calcular_suma_serie_factorial(int n) {
    double suma = 0;
    for (int i = 1; i <= n; ++i) {
        int factorial = calcular_factorial(i);
        suma += static_cast<double>(i) / factorial;
    }
    return suma;
}

int main() {
    int n = 5;
    std::cout << "La suma de la serie factorial hasta " << n << " es " << calcular_suma_serie_factorial(n) << std::endl;
    return 0;
}