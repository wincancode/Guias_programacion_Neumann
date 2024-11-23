// 7. Un capital C se coloca a un interés anual R. Al cabo de cuantos años se doblará?

#include <iostream>
using namespace std;

int main() {
    double capital, interes;
    int años = 0;
    cout << "Ingrese el capital: ";
    cin >> capital;
    cout << "Ingrese el interés anual: ";
    cin >> interes;

    double objetivo = capital * 2;
    while (capital < objetivo) {
        capital += capital * interes;
        años++;
    }

    cout << "El capital se doblará en " << años << " años." << endl;
    return 0;
}