#include <stdio.h>

struct trabajador{
	char nombre[20];
	char apaterno[20];
	char amaterno[20];
	char CURP[19];
	char puesto[20];
	int edad;
	float salario;
};
struct trabajador n1;

void main(){
printf("Ingresa el NOMBRE del trabajador: ");
scanf("%s", &n1.nombre);
printf("Ingresa el apellido paterno del trabajador: ");
scanf("%s", &n1.apaterno);
printf("Ingresa el apellido materno del trabajador: ");
scanf("%s", &n1.amaterno);
printf("Ingresa la CURP del trabajador: ");
scanf("%s", &n1.CURP);
printf("Ingrese el puesto del trabajador: ");
scanf("%s", &n1.puesto);
printf("Ingresa el salario del trabajador: ");
scanf("%f", &n1.salario);

printf("\nDatos del trabajador: \n");
printf("Nombre: %s %s %s \n", n1.nombre, n1.apaterno, n1.amaterno);
printf("CURP: %s \n", n1.CURP);
printf("Puesto en la empresa: %s \n", n1.puesto);
printf("Salario: %.2f \n", n1.salario);
	






}
