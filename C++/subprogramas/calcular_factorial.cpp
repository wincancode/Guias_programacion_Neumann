
#include <iostream>

int calcular_factorial(int n) {
    int factorial = 1;
    for (int i = 1; i <= n; ++i) {
        factorial *= i;
    }
    return factorial;
}

int main() {
    int n = 5;
    std::cout << "El factorial de " << n << " es " << calcular_factorial(n) << std::endl;
    return 0;
}