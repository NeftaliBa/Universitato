/*
* 14 de agosto de 2024
* Programa para calcular la raiz cuadratica
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>

// Funcion para calcular la raiz cuadratica media (RMS)
double calcularRMS(const std::vector<double>& datos) {
    double sumaCuadrados = 0.0;
    int N = datos.size();

    for (std::vector<double>::const_iterator it = datos.begin(); it != datos.end(); ++it) {
        sumaCuadrados += (*it) * (*it);
    }

    return std::sqrt(sumaCuadrados / N);
}

// Funci�n para leer datos desde un archivo CSV
std::vector<double> leerDatosCSV(const std::string& archivoDatos) {
    std::vector<double> datos;
    std::ifstream archivo(archivoDatos.c_str()); // Convertir std::string a const char*
    std::string linea;

    while (std::getline(archivo, linea)) {
        std::stringstream ss(linea);
        std::string valor;

        while (std::getline(ss, valor, ',')) {
            double valorNumerico;
            std::stringstream ssValor(valor);
            ssValor >> valorNumerico;
            datos.push_back(valorNumerico);
        }
    }

    return datos;
}

int main() {
    // Nombre del archivo CSV
    std::string archivoDatos = "datosActividad.csv";

    // Leer los datos del archivo CSV
    std::vector<double> datos = leerDatosCSV(archivoDatos);

    // C�lculo del RMS
    double rms = calcularRMS(datos);

    // Mostrar el resultado
    std::cout << "La raiz cuadratica media (RMS) es: " << rms << std::endl;

    return 0;
}

