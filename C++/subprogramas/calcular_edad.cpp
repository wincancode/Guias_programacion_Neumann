
#include <iostream>
#include <ctime>

int calcular_edad(int dia_nacimiento, int mes_nacimiento, int anio_nacimiento) {
    time_t t = time(nullptr);
    tm* fecha_actual = localtime(&t);

    int edad = fecha_actual->tm_year + 1900 - anio_nacimiento;
    if (fecha_actual->tm_mon + 1 < mes_nacimiento || (fecha_actual->tm_mon + 1 == mes_nacimiento && fecha_actual->tm_mday < dia_nacimiento)) {
        edad -= 1;
    }
    return edad;
}

int main() {
    int dia_nacimiento = 15;
    int mes_nacimiento = 6;
    int anio_nacimiento = 1990;
    std::cout << "La edad es " << calcular_edad(dia_nacimiento, mes_nacimiento, anio_nacimiento) << std::endl;
    return 0;
}