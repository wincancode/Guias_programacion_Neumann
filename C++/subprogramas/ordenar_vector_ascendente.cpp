
#include <iostream>
#include <vector>

using namespace std;

void ordenar_vector_ascendente(vector<int>& vector) {
    for (size_t i = 0; i < vector.size(); ++i) {
        for (size_t j = i + 1; j < vector.size(); ++j) {
            if (vector[i] > vector[j]) {
                swap(vector[i], vector[j]);
            }
        }
    }
}

int main() {
    vector<int> vector = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    ordenar_vector_ascendente(vector);
    cout << "Vector ordenado: ";
    for (int val : vector) {
        cout << val << " ";
    }
    cout << endl;
    return 0;
}