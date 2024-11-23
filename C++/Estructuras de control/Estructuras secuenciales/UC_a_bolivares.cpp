
/*
1. Escriba un programa que calcule y escriba el valor en bolívares de una cantidad dada de
unidades tributarias (1 U.T. =1.500,00).
*/

#include <iostream>
using namespace std;

int main() {
    // Declaracion de variables
    int valor_ut = 1500;
    int cantidad_ut = 0;
    int valor_bolivares = 0;

    // Entrada de datos
    cout << "Ingrese la cantidad de unidades tributarias: ";
    cin >> cantidad_ut;

    // Proceso
    valor_bolivares = valor_ut * cantidad_ut;

    // Salida
    cout << "El valor en bolivares de " << cantidad_ut << " unidades tributarias es: " << valor_bolivares << endl;

    return 0;
}