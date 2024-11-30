
#include <iostream>
#include <vector>

using namespace std;

void transformar_filas_a_columnas(vector<vector<int>>& matriz_inicial) {
    vector<vector<int>> matriz_final(matriz_inicial[0].size(), vector<int>(matriz_inicial.size()));
    for (size_t j = 0; j < matriz_inicial[0].size(); ++j) {
        for (size_t i = 0; i < matriz_inicial.size(); ++i) {
            matriz_final[j][i] = matriz_inicial[i][j];
        }
    }

    cout << "Matriz Inicial:" << endl;
    for (const auto& fila : matriz_inicial) {
        for (int val : fila) {
            cout << val << " ";
        }
        cout << endl;
    }

    cout << "Matriz Final:" << endl;
    for (const auto& fila : matriz_final) {
        for (int val : fila) {
            cout << val << " ";
        }
        cout << endl;
    }
}

int main() {
    vector<vector<int>> matriz_inicial = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };
    transformar_filas_a_columnas(matriz_inicial);
    return 0;
}