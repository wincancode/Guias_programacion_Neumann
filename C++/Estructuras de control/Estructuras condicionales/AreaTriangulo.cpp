
// . Diseñar un algoritmo que calcule el área de un triangulo en función de las
// longitudes de sus lados.
// Area = sqrt(s * (s - a) * (s - b) * (s - c)), donde s = (a + b + c) / 2 y a, b y c son los lados del triángulo.

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // Entradas
    float a, b, c;
    cout << "Ingrese la longitud del lado a: ";
    cin >> a;
    cout << "Ingrese la longitud del lado b: ";
    cin >> b;
    cout << "Ingrese la longitud del lado c: ";
    cin >> c;

    // Procesos
    float s = (a + b + c) / 2;
    float area = sqrt(s * (s - a) * (s - b) * (s - c));

    // Salidas
    cout << "El área del triángulo con lados de longitud " << a << ", " << b << " y " << c << " es: " << area << endl;

    return 0;
}