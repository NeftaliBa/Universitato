/*
* 14 de agosto de 2024 
* Neftali Barrera Rodriguez 
* Programa para calcular la raiz cuadratica 
*/

#include <iostream>
#include <vector>
#include <cmath>

// Funcion para calcular la raiz cuadratica
double calcularRMS(const std::vector<double>& datos) {
    double sumaCuadrados = 0.0;
    int N = datos.size();

    for (double x : datos) {
        sumaCuadrados += x * x;
    }

    return std::sqrt(sumaCuadrados / N);
}

int main() {
    // Se ingresan los datos
    std::vector<double> datos = 
    {0, 
	35.1162579629031, 
	68.8830178257162, 
	100.002641943528, 
	127.279220613579, 
	149.664530214458, 
	166.298315852032, 
	176.541350472581, 
	180.0, 
	176.541350472581, 
	166.298315852032, 
	149.664530214458, 
	127.279220613579, 
	100.002641943528, 
	68.8830178257162, 
	35.1162579629032, 
	1.01979700157664e-13, 
	-35.116257962903, 
	-68.8830178257161, 
	-100.002641943528, 
	-127.279220613578, 
	-149.664530214458, 
	-166.298315852032, 
	-176.541350472581, 
	-180.0,
	-176.541350472582, 
	-166.298315852032, 
	-149.664530214458, 
	-127.279220613579,
	-100.002641943529, 
	-68.8830178257163, 
	-35.1162579629033, 
	-2.03959400315327e-13};

    // Se manda a llamar a la funcion calcularRMS
    double rms = calcularRMS(datos);

    // Mostrar el resultado 
    std::cout << "La raiz cuadratica media (RMS) es: " << rms << std::endl;

    return 0;
}

