
#include <iostream>
#include "es_primo.cpp"

using namespace std;

void numeros_primos_fibonacci(int n) {
    int a = 0, b = 1;
    while (a <= n) {
        if (es_primo(a)) {
            cout << a << " ";
        }
        int temp = a;
        a = b;
        b = temp + b;
    }
    cout << endl;
}

int main() {
    int n;
    cout << "Ingrese el valor de n: ";
    cin >> n;
    cout << "Números primos en la sucesión de Fibonacci hasta " << n << ": ";
    numeros_primos_fibonacci(n);
    return 0;
}