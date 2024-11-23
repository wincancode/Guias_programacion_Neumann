
/*
4. Una tienda ofrece un descuento de 15% sobre el monto de compra para sus clientes, elabore
un programa que calcule el porcentaje de descuento de esa compra, el monto a pagar por el
IVA (16% de IVA) y finalmente el total a pagar
*/

#include <iostream>
using namespace std;

int main() {
    // Declaracion de variables
    float monto_compra = 0;
    float descuento = 0;
    float monto_iva = 0;
    float total_pagar = 0;

    // Entrada de datos
    cout << "Ingrese el monto de compra: ";
    cin >> monto_compra;

    // Proceso
    descuento = monto_compra * 0.15;
    monto_iva = monto_compra * 0.16;
    total_pagar = monto_compra - descuento + monto_iva;

    // Salida
    cout << "El porcentaje de descuento de la compra es: " << descuento << endl;
    cout << "El monto a pagar por el IVA es: " << monto_iva << endl;
    cout << "El total a pagar es: " << total_pagar << endl;

    return 0;
}