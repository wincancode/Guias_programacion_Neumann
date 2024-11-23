
//3 Diseñar un algoritmo para resolver una ecuación de segundo grado.

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // Entradas
    cout << "Ecuación de segundo grado" << endl;
    float a, b, c;
    cout << "Ingrese el valor de a: ";
    cin >> a;
    cout << "Ingrese el valor de b: ";
    cin >> b;
    cout << "Ingrese el valor de c: ";
    cin >> c;

    // Procesos
    string solucion;
    if (a == 0) {
        if (b == 0) {
            if (c == 0) {
                solucion = "Infinitas soluciones";
            } else {
                solucion = "No tiene solución";
            }
        } else {
            solucion = -c / b;
            cout << "La solución es: " << solucion;
        }
    } else {
        float discriminante = b * b - 4 * a * c;
        if (discriminante < 0) {
            solucion = "No tiene solución";
        } else if (discriminante == 0) {
            solucion = -b / (2 * a);
        } else {
            float solucion1 = (-b + sqrt(discriminante)) / (2 * a);
            float solucion2 = (-b - sqrt(discriminante)) / (2 * a);
            cout << "Las soluciones son: " << solucion1 << " y " << solucion2;
        }
    }

    return 0;
}