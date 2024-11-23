
// Se introduce por teclado una hora determinada con el formato H, M, S. Se pide
// calcular la hora que será dentro de un segundo.

#include <iostream>
using namespace std;

int main() {
    // Entradas
    int hora, minutos, segundos;
    cout << "Ingrese la hora: ";
    cin >> hora;
    cout << "Ingrese los minutos: ";
    cin >> minutos;
    cout << "Ingrese los segundos: ";
    cin >> segundos;

    // Proceso
    if (segundos == 59) {
        segundos = 0;
        if (minutos == 59) {
            minutos = 0;
            if (hora == 23) {
                hora = 0;
            } else {
                hora += 1;
            }
        } else {
            minutos += 1;
        }
    } else {
        segundos += 1;
    }

    // Salidas
    cout << "La hora dentro de un segundo será: " << hora << ":" << minutos << ":" << segundos << endl;

    return 0;
}