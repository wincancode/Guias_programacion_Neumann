// Dada una secuencia de enteros terminada en cero, elabore un algoritmo para
// resolver cada uno de los siguientes problemas:
// a) Calcular el promedio de dicha secuencia.
// b) Calcular el porcentaje de números impares y el porcentaje de números pares.
// c) Calcular la cantidad de valores iguales a un valor N dado por el usuario.
// d) Contar la cantidad de números primos.

#include <iostream>
using namespace std;

int main() {
    int N, num, suma_numeros = 0, cantidad_numeros = 0, cantidad_impares = 0, cantidad_pares = 0, cantidad_iguales_N = 0, cantidad_primos = 0;
    cout << "Ingrese un numero entero: ";
    cin >> N;

    cout << "Si ingresa un cero, se terminara el programa." << endl;
    cout << "Ingrese un numero: ";
    cin >> num;
    while (num != 0) {
        suma_numeros += num;
        cantidad_numeros++;

        // Verificar pares e impares
        if (num % 2 == 0) {
            cantidad_pares++;
        } else {
            cantidad_impares++;
        }

        // Verificar numeros iguales a N
        if (num == N) {
            cantidad_iguales_N++;
        }

        // Verificar numeros primos
        if (num > 1) {
            bool es_primo = true;
            for (int i = 2; i < num; i++) {
                if (num % i == 0) {
                    es_primo = false;
                    break;
                }
            }
            if (es_primo) {
                cantidad_primos++;
            }
        }
        cout << "Ingrese un numero: ";
        cin >> num;
    }

    double promedio = static_cast<double>(suma_numeros) / cantidad_numeros;
    double porcentaje_impares = (static_cast<double>(cantidad_impares) / cantidad_numeros) * 100;
    double porcentaje_pares = (static_cast<double>(cantidad_pares) / cantidad_numeros) * 100;

    cout << "El promedio de la secuencia es: " << promedio << endl;
    cout << "El porcentaje de numeros impares es: " << porcentaje_impares << "%" << endl;
    cout << "El porcentaje de numeros pares es: " << porcentaje_pares << "%" << endl;
    cout << "La cantidad de numeros iguales a N es: " << cantidad_iguales_N << endl;
    cout << "La cantidad de numeros primos es: " << cantidad_primos << endl;

    return 0;
}