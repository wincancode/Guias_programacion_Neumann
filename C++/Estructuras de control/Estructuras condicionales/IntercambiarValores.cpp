
// Realizar un algoritmo que permita intercambiar entre si los valores de dos
// variables A y B.

#include <iostream>
using namespace std;

int main() {
    // Entradas
    float a, b;
    cout << "Ingrese el valor de la variable A: ";
    cin >> a;
    cout << "Ingrese el valor de la variable B: ";
    cin >> b;

    // Procesos
    float temp = a;
    a = b;
    b = temp;

    // Salidas
    cout << "El valor de A es: " << a << endl;
    cout << "El valor de B es: " << b << endl;

    return 0;
}