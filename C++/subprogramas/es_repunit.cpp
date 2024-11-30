
#include <iostream>
#include <string>

using namespace std;

bool es_repunit(int numero) {
    string str_num = to_string(numero);
    return str_num.find_first_not_of('1') == string::npos;
}

int main() {
    int numero;
    cout << "Ingrese un número: ";
    cin >> numero;
    cout << "¿Es " << numero << " un número Repunit? " << (es_repunit(numero) ? "Sí" : "No") << endl;
    return 0;
}