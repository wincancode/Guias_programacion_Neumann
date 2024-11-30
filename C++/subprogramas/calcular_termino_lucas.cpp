
#include <iostream>

int calcular_termino_lucas(int n) {
    if (n == 0) {
        return 2;
    } else if (n == 1) {
        return 1;
    } else {
        int termino_anterior = 2;
        int termino_actual = 1;
        for (int i = 2; i <= n; ++i) {
            int termino_siguiente = termino_anterior + termino_actual;
            termino_anterior = termino_actual;
            termino_actual = termino_siguiente;
        }
        return termino_actual;
    }
}

int main() {
    int n = 6;
    std::cout << "El término " << n << "-ésimo de la secuencia de Lucas es " << calcular_termino_lucas(n) << std::endl;
    return 0;
}