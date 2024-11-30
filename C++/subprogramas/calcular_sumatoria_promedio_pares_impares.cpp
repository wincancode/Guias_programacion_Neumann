
#include <iostream>
#include <vector>

void calcular_sumatoria_promedio_pares_impares(const std::vector<int>& numeros) {
    int sumatoria_pares = 0;
    int sumatoria_impares = 0;
    int cantidad_pares = 0;
    int cantidad_impares = 0;

    for (int numero : numeros) {
        if (numero % 2 == 0) {
            sumatoria_pares += numero;
            cantidad_pares += 1;
        } else {
            sumatoria_impares += numero;
            cantidad_impares += 1;
        }
    }

    double promedio_pares = cantidad_pares > 0 ? static_cast<double>(sumatoria_pares) / cantidad_pares : 0;
    double promedio_impares = cantidad_impares > 0 ? static_cast<double>(sumatoria_impares) / cantidad_impares : 0;

    double porcentaje_pares = static_cast<double>(cantidad_pares) / numeros.size() * 100;
    double porcentaje_impares = static_cast<double>(cantidad_impares) / numeros.size() * 100;

    std::cout << "Sumatoria pares: " << sumatoria_pares << ", Sumatoria impares: " << sumatoria_impares << std::endl;
    std::cout << "Promedio pares: " << promedio_pares << ", Promedio impares: " << promedio_impares << std::endl;
    std::cout << "Porcentaje pares: " << porcentaje_pares << "%, Porcentaje impares: " << porcentaje_impares << "%" << std::endl;
}

int main() {
    std::vector<int> numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    calcular_sumatoria_promedio_pares_impares(numeros);
    return 0;
}