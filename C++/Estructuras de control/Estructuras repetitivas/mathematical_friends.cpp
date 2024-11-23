// La amistad cuadrática entre números se podría explicar en la siguiente
// conversación entre el numero 13 y el numero 16
// 16 al 13: Quiero ofrecerte mi homenaje amigo, mi cuadrado es 256 cuya suma
// de guarismos es 13
// 13 al 16: Agradezco tu bondad y quiero retribuirla en la misma forma. Mi
// cuadrado es 169 cuya suma de guarismos es 16.
// Dado este pequeño fragmento de “El hombre que calculaba” realice un programa que
// diga si dos números son amigos matemáticos

#include <iostream>
using namespace std;

int main() {
    int num1, num2, cuadrado1, cuadrado2, suma1 = 0, suma2 = 0;
    cout << "Ingrese el primer número: ";
    cin >> num1;
    cout << "Ingrese el segundo número: ";
    cin >> num2;

    cuadrado1 = num1 * num1;
    cuadrado2 = num2 * num2;

    while (cuadrado1 != 0) {
        suma1 += cuadrado1 % 10;
        cuadrado1 /= 10;
    }

    while (cuadrado2 != 0) {
        suma2 += cuadrado2 % 10;
        cuadrado2 /= 10;
    }

    if (suma1 == num2 && suma2 == num1) {
        cout << "Los números son amigos matemáticos." << endl;
    } else {
        cout << "Los números no son amigos matemáticos." << endl;
    }

    return 0;
}