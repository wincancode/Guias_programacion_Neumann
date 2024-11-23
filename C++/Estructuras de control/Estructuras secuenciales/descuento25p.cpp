
/*
2. Una tienda ofrece un descuento de 25% sobre el monto de compra para sus clientes, elabore
un programa que calcule el porcentaje de descuento de esa compra.
*/

#include <iostream>
using namespace std;

int main() {
    // Declaracion de variables
    float monto_compra = 0;
    float descuento = 0;

    // Entrada de datos
    cout << "Ingrese el monto de compra: ";
    cin >> monto_compra;

    // Proceso
    descuento = monto_compra * 0.25;

    // Salida
    cout << "El porcentaje de descuento de la compra es: " << descuento << endl;

    return 0;
}