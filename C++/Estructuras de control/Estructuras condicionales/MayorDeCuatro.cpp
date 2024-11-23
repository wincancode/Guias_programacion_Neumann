
//4 Escribir un algoritmo que lea cuatro números y a continuación imprima el mayor de
//ellos.

#include <iostream>
using namespace std;

int main() {
    // Entradas
    float num1, num2, num3, num4;
    cout << "Ingrese el primer número: ";
    cin >> num1;
    cout << "Ingrese el segundo número: ";
    cin >> num2;
    cout << "Ingrese el tercer número: ";
    cin >> num3;
    cout << "Ingrese el cuarto número: ";
    cin >> num4;

    // Procesos
    float mayor;
    if (num1 >= num2 && num1 >= num3 && num1 >= num4) {
        mayor = num1;
    } else if (num2 >= num1 && num2 >= num3 && num2 >= num4) {
        mayor = num2;
    } else if (num3 >= num1 && num3 >= num2 && num3 >= num4) {
        mayor = num3;
    } else {
        mayor = num4;
    }

    // Salidas
    cout << "El número mayor es: " << mayor << endl;

    return 0;
}