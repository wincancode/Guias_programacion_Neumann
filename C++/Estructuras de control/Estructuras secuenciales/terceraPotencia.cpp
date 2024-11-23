
/*
6. Diseñe un programa que permita calcular la tercera potencia de un número entero dado.
*/

#include <iostream>
using namespace std;

int main() {
    // Declaracion de variables
    int numero = 0;
    int tercera_potencia = 0;

    // Entrada de datos
    cout << "Ingrese un número entero: ";
    cin >> numero;

    // Proceso
    tercera_potencia = numero * numero * numero;

    // Salida
    cout << "La tercera potencia de " << numero << " es: " << tercera_potencia << endl;

    return 0;
}