
// 2. Escriba un Algoritmo, que determine el monto a pagar de una llamada
// telefónica teniendo en cuenta lo siguiente: toda llamada que dure hasta 3
// minutos tiene un costo de 35 Bs. Por cada minuto adicional se cobra una
// tarifa de 15 Bs. Se debe leer el tiempo de llamadas en el formato hh:mm.
// Salida: tiempo de llamada y costo

#include <iostream>
using namespace std;

int main() {
    // Entradas
    cout << "Calculadora de llamadas" << endl;
    int horas, minutos;
    cout << "Ingrese las horas de la llamada: ";
    cin >> horas;
    cout << "Ingrese los minutos de la llamada: ";
    cin >> minutos;

    // Procesos
    int costo;
    if (horas == 0) {
        costo = 35;
    } else {
        costo = 35 + (horas - 1) * 60 * 15;
    }
    if (minutos > 3) {
        costo += (minutos - 3) * 15;
    }

    int tiempo_llamada = horas * 60 + minutos;

    // Salidas
    cout << "Tiempo de llamada: " << tiempo_llamada << " minutos" << endl;
    cout << "Costo: " << costo << endl;

    return 0;
}