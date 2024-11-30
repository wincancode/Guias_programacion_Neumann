
#include <iostream>
#include <cmath>
#include "es_primo.cpp"

using namespace std;

bool es_primo_mersenne(int numero) {
    if (!es_primo(numero)) {
        return false;
    }
    int mersenne = pow(2, numero) - 1;
    return es_primo(mersenne);
}

int main() {
    int numero;
    cout << "Ingrese un número: ";
    cin >> numero;
    cout << "¿Es " << numero << " un número primo de Mersenne? " << (es_primo_mersenne(numero) ? "Sí" : "No") << endl;
    return 0;
}