// Dado un número entero de N dígitos, se pide que construya un algoritmo que
// substituya todas las ocurrencias de un dígito dado X por otro dígito
// suministrado Y.
// Ejemplo:
// Entrada Salida
// 14123 64623
// X=1
// Y=6

#include <iostream>
using namespace std;

int main() {
    int n, x, y, nuevo_numero = 0, multiplo = 1;
    cout << "Ingrese un número entero: ";
    cin >> n;
    cout << "Ingrese el dígito a reemplazar: ";
    cin >> x;
    cout << "Ingrese el dígito por el que reemplazar: ";
    cin >> y;

    while (n > 0) {
        int digito = n % 10;
        if (digito == x) {
            digito = y;
        }
        nuevo_numero = digito * multiplo + nuevo_numero;
        n /= 10;
        multiplo *= 10;
        cout << "Digito: " << digito << ", Nuevo número: " << nuevo_numero << endl;
    }

    cout << "El número resultante es " << nuevo_numero << "." << endl;
    return 0;
}