
// 2. Escriba el algoritmo para simular una calculadora. Se debe leer los operandos y el
// operador. 

#include <iostream>
using namespace std;

int main() {
    // Entradas
    cout << "Calculadora" << endl;
    float num1, num2;
    char operador;
    cout << "Ingrese el primer número: ";
    cin >> num1;
    cout << "Ingrese el segundo número: ";
    cin >> num2;
    cout << "Ingrese el operador: ";
    cin >> operador;

    // Procesos
    float resultado;
    if (operador == '+') {
        resultado = num1 + num2;
    } else if (operador == '-') {
        resultado = num1 - num2;
    } else if (operador == '*') {
        resultado = num1 * num2;
    } else if (operador == '/') {
        resultado = num1 / num2;
    } else {
        cout << "Operador no válido" << endl;
        return 1;
    }

    // Salidas
    cout << "El resultado de " << num1 << " " << operador << " " << num2 << " es: " << resultado << endl;

    return 0;
}