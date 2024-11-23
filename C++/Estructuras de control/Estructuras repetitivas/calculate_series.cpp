// # Escriba un algoritmo que calcule el resultado de la siguiente serie:
// a) 2, 5, 7, 10, 12, 15, 17, 20, …. 1800
// b) 1+ 1/2 + 1/3 + 1/4 + ... + 1/n
// c) 1 - 1/2 + 1/3 - 1/4 + ... + 1/n

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingrese la cantidad de números de la serie: ";
    cin >> n;

    // a)
    int suma = 0;
    for (int i = 2; i <= 1800; i += 3) {
        suma += i;
    }
    cout << "La suma de la serie es " << suma << endl;

    // b)
    double suma_b = 0;
    for (int i = 1; i <= n; i++) {
        suma_b += 1.0 / i;
    }
    cout << "La suma de la serie es " << suma_b << endl;

    // c)
    double suma_c = 0;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            suma_c -= 1.0 / i;
        } else {
            suma_c += 1.0 / i;
        }
    }
    cout << "La suma de la serie es " << suma_c << endl;

    return 0;
}