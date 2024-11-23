`
// El menú de un restaurante de comida rápida es:
// Hamburguesa250 Ptas.
// Cerveza 100 Ptas.
// Coca cola 125 Ptas.
// Ensalada 200 Ptas.
// Salchichas 275 Ptas.
// Sopa 260 Ptas.
// Pastel 300 Ptas.
// Se desea un algoritmo que calcule las ventas totales al final del día, así como los
// impuestos a pagar (12%). El algoritmo tendrá como entrada el número de cada uno e
// los productos vendidos ese día. 

#include <iostream>
using namespace std;

int main() {
    // Entradas
    int hamburguesas, cervezas, cocas, ensaladas, salchichas, sopas, pasteles;
    double impuesto = 0.12;
    cout << "Ingrese el número de hamburguesas vendidas: ";
    cin >> hamburguesas;
    cout << "Ingrese el número de cervezas vendidas: ";
    cin >> cervezas;
    cout << "Ingrese el número de cocas vendidas: ";
    cin >> cocas;
    cout << "Ingrese el número de ensaladas vendidas: ";
    cin >> ensaladas;
    cout << "Ingrese el número de salchichas vendidas: ";
    cin >> salchichas;
    cout << "Ingrese el número de sopas vendidas: ";
    cin >> sopas;
    cout << "Ingrese el número de pasteles vendidos: ";
    cin >> pasteles;

    // Procesos
    int total = hamburguesas * 250 + cervezas * 100 + cocas * 125 + ensaladas * 200 + salchichas * 275 + sopas * 260 + pasteles * 300;
    double impuestos = total * impuesto;
    double ventas_tot = total - impuestos;

    // Salidas
    cout << "Las ventas totales del día son: " << ventas_tot << endl;
    cout << "Los impuestos a pagar son: " << impuestos << endl;

    return 0;
}