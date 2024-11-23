// 0. Por cada uno de los N estudiantes se tienen la nota obtenida en una materia hacer
// un algoritmo que obtenga: la nota máxima, la mínima, cuántos perdieron y cuántos
// ganaron la asignatura.

#include <iostream>
using namespace std;

int main() {
    int n, perdieron = 0, ganaron = 0;
    cout << "Ingrese la cantidad de estudiantes: ";
    cin >> n;

    double nota_max, nota_min;
    for (int i = 0; i < n; i++) {
        double nota;
        cout << "Ingrese la nota del estudiante " << i + 1 << ": ";
        cin >> nota;
        if (i == 0) {
            nota_max = nota;
            nota_min = nota;
        } else {
            if (nota > nota_max) {
                nota_max = nota;
            }
            if (nota < nota_min) {
                nota_min = nota;
            }
        }
        if (nota < 10) {
            perdieron++;
        } else {
            ganaron++;
        }
    }

    cout << "La nota máxima es " << nota_max << "." << endl;
    cout << "La nota mínima es " << nota_min << "." << endl;
    cout << "Perdieron " << perdieron << " estudiantes." << endl;
    cout << "Ganaron " << ganaron << " estudiantes." << endl;

    return 0;
}