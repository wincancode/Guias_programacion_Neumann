// Construya un algoritmo utilizando estructuras iterativas que calculen el factorial de
// un número entero positivo n. La función factorial, representada por n!, es ampliamente
// utilizada, y se especifica que n!= n*(n-1)!, y además 0!=1.

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingrese un número entero positivo: ";
    cin >> n;

    if (n < 0) {
        cout << "El número ingresado no es positivo." << endl;
    } else {
        long long factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }
        cout << "El factorial de " << n << " es " << factorial << "." << endl;
    }

    return 0;
}