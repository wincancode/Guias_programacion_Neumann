
// . Leer tres números del teclado y deducir si se han introducido en orden creciente.

#include <iostream>
using namespace std;

int main() {
    // Entradas
    int num1, num2, num3;
    cout << "Ingrese el primer número: ";
    cin >> num1;
    cout << "Ingrese el segundo número: ";
    cin >> num2;
    cout << "Ingrese el tercer número: ";
    cin >> num3;

    // Proceso
    if (num1 < num2 && num2 < num3) {
        cout << "Los números están en orden creciente." << endl;
    } else if (num1 > num2 && num2 > num3) {
        cout << "Los números están en orden decreciente." << endl;
    } else {
        cout << "Los números no están en orden creciente ni decreciente." << endl;
    }

    return 0;
}