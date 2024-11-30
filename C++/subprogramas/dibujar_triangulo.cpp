
#include <iostream>

/*
7. Escriba un procedimiento que permita dibujar un triángulo como el que se muestra a
continuación, debe ser de altura h y esta debe ser recibida como parámetro:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
*/

void dibujar_triangulo(int h) {
    int numero = 1;
    for (int i = 1; i <= h; ++i) {
        for (int j = 0; j < i; ++j) {
            std::cout << numero << " ";
            ++numero;
        }
        std::cout << std::endl;
    }
}

int main() {
    int h = 5;
    dibujar_triangulo(h);
    return 0;
}