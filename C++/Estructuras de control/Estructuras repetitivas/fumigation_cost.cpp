// Una empresa extranjera de aviación fumiga cosechas contra una gran variedad de
// plagas. Los valores cobrados a los granjeros dependen de lo que éste desea fumigar y
// de cuántas hectáreas se fumigan, de acuerdo a la siguiente distribución:
// Tipo 1: fumigación contra malas hierbas, $10 por hectárea.
// Tipo 2: fumigación contra langostas, $15 hectárea.
// Tipo 3: fumigación contra malas gusanos, $20 por hectárea.
// Tipo 4: fumigación contra todo lo anterior, $30 por hectárea.
// Si el área a fumigar es mayor de 1000 hectáreas, el granjero goza de un 5% de
// descuento. Además, cualquier granjero cuya cuenta sobrepase los $3000 se le
// descuenta un 10% sobre la cantidad que exceda dicho precio. Si se aplican ambos
// conceptos, el correspondiente a la superficie se considera primero. Por cada pedido se
// tiene la siguiente información: nombre del granjero, tipo de fumigación solicitada
// (1,2,3,4) y el número de hectáreas a fumigar. Por cada solicitud se debe suministrar:
// nombre del granjero y valor a pagar.

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingrese la cantidad de pedidos: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        string granjero;
        int tipo, hectareas;
        double valor = 0;
        cout << "Ingrese el nombre del granjero: ";
        cin >> granjero;
        cout << "Ingrese el tipo de fumigación (1, 2, 3, 4): ";
        cin >> tipo;
        cout << "Ingrese la cantidad de hectáreas a fumigar: ";
        cin >> hectareas;

        if (tipo == 1) {
            valor = 10 * hectareas;
        } else if (tipo == 2) {
            valor = 15 * hectareas;
        } else if (tipo == 3) {
            valor = 20 * hectareas;
        } else if (tipo == 4) {
            valor = 30 * hectareas;
        }

        if (hectareas > 1000) {
            valor *= 0.95;
        }

        if (valor > 3000) {
            valor = 3000 + (valor - 3000) * 0.9;
        }

        cout << "El granjero " << granjero << " debe pagar $" << valor << "." << endl;
    }

    return 0;
}