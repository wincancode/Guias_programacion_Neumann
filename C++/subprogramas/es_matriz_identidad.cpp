
#include <iostream>
#include <vector>

using namespace std;

bool es_matriz_identidad(const vector<vector<int>>& matriz) {
    for (size_t i = 0; i < matriz.size(); ++i) {
        for (size_t j = 0; j < matriz[i].size(); ++j) {
            if ((i == j && matriz[i][j] != 1) || (i != j && matriz[i][j] != 0)) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    vector<vector<int>> matriz = {
        {1, 0, 0, 0},
        {0, 1, 0, 0},
        {0, 0, 1, 0},
        {0, 0, 0, 1}
    };
    cout << "¿Es la matriz identidad? " << (es_matriz_identidad(matriz) ? "Sí" : "No") << endl;
    return 0;
}