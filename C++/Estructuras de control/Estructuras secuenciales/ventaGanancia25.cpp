
/*
3. Un revendedor compra un artículo a un precio determinado. Obtener el precio en que lo debe
vender para obtener una ganancia del 25%
*/

#include <iostream>
using namespace std;

int main() {
    // Declaracion de variables
    float precio_compra = 0;
    float precio_venta = 0;

    // Entrada de datos
    cout << "Ingrese el precio de compra del artículo: ";
    cin >> precio_compra;

    // Proceso
    precio_venta = precio_compra * 1.25;

    // Salida
    cout << "El precio de venta para obtener una ganancia del 25% es: " << precio_venta << endl;

    return 0;
}