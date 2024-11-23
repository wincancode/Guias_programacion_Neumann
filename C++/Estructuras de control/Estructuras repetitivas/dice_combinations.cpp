// Con dos dados al azar se pueden obtener los números: 2..12. Por ejemplo, para
// obtener el número 2, la única forma es que ambos salgan con el uno; para obtener un
// cuatro existen dos combinaciones posibles, que ambos tengan un dos o que un dado
// salga con uno y el otro con tres. Diseñe un algoritmo (utilizando estructuras iterativas)
// que leyendo un valor N, validado entre 2 y 12, genere cuáles son las combinaciones
// posibles, sin repetición, para ese valor.

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingrese un número entre 2 y 12: ";
    cin >> n;
    while (n < 2 || n > 12) {
        cout << "Ingrese un número entre 2 y 12: ";
        cin >> n;
    }
    for (int i = 1; i <= 6; i++) {
        for (int j = 1; j <= 6; j++) {
            if (i + j == n) {
                cout << "(" << i << ", " << j << ")" << endl;
            }
        }
    }
    return 0;
}