
/*
16. Diseñar un programa que permita calcular ab, donde a y b son valores enteros.
*/

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // Declaracion de variables
    int a = 0;
    int b = 0;
    int resultado = 0;

    // Entrada de datos
    cout << "Ingrese el valor de a: ";
    cin >> a;
    cout << "Ingrese el valor de b: ";
    cin >> b;

    // Proceso
    resultado = pow(a, b);

    // Salida
    cout << "El resultado de " << a << " elevado a la potencia " << b << " es: " << resultado << endl;

    return 0;
}