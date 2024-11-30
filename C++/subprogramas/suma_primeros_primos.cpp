
#include <iostream>
#include "es_primo.cpp"

using namespace std;

int suma_primeros_primos(int n) {
    int suma = 0;
    int contador = 0;
    int numero = 2;
    while (contador < n) {
        if (es_primo(numero)) {
            suma += numero;
            contador++;
        }
        numero++;
    }
    return suma;
}

int main() {
    int n;
    cout << "Ingrese el valor de N: ";
    cin >> n;
    cout << "La suma de los primeros " << n << " números primos es: " << suma_primeros_primos(n) << endl;
    return 0;
}