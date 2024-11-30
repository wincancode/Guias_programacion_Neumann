
#include <iostream>
#include <vector>

void encontrar_menor_valor(const std::vector<int>& vector) {
    int menor_valor = vector[0];
    int posicion_menor_valor = 0;
    for (size_t i = 1; i < vector.size(); ++i) {
        if (vector[i] < menor_valor) {
            menor_valor = vector[i];
            posicion_menor_valor = i;
        }
    }
    std::cout << "El menor valor es " << menor_valor << " y se encuentra en la posición " << posicion_menor_valor << std::endl;
}

int main() {
    std::vector<int> vector = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    encontrar_menor_valor(vector);
    return 0;
}