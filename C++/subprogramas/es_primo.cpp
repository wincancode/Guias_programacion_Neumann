
#include <cmath>

bool es_primo(int numero) {
    if (numero < 2) {
        return false;
    }
    for (int i = 2; i <= sqrt(numero); ++i) {
        if (numero % i == 0) {
            return false;
        }
    }
    return true;
}