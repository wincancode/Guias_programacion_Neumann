
#include <iostream>
#include <string>

using namespace std;

bool es_palindromo(const string& str) {
    return str == string(str.rbegin(), str.rend());
}

int main() {
    string str = "radar";
    cout << "¿Es '" << str << "' un palíndromo? " << (es_palindromo(str) ? "Sí" : "No") << endl;
    return 0;
}