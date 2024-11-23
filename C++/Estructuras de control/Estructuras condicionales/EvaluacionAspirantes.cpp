
// Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de
// ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que
// obtenga una calificación mayor que a un mínimo dado en cualquiera de los
// exámenes es aceptado; en caso contrario es rechazado. Realice un
// Algoritmo, que lea el nombre y calificaciones del aspirante. Realice un
// Algoritmo, que indique si es aceptado o rechazado. (Ejemplo mínimo = 90)

#include <iostream>
#include <string>
using namespace std;

int main() {
    // Entradas
    string nombre;
    float c1, c2, minimo;
    cout << "Ingrese el nombre del aspirante: ";
    cin >> nombre;
    cout << "Ingrese la calificación del primer examen: ";
    cin >> c1;
    cout << "Ingrese la calificación del segundo examen: ";
    cin >> c2;
    cout << "Ingrese la calificación mínima: ";
    cin >> minimo;

    // Procesos
    string resultado;
    if (c1 >= minimo || c2 >= minimo) {
        resultado = "Aceptado";
    } else {
        resultado = "Rechazado";
    }

    // Salidas
    cout << "El aspirante " << nombre << " ha sido " << resultado << endl;

    return 0;
}