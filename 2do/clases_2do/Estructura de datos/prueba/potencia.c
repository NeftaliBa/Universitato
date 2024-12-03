#include <math.h>
#include <stdio.h>


int main()
{
	int n, p, e; // Aquí guardaremos lo que ingrese el usuario
	printf("Ingresa el numero: ");
	scanf("%d", &n);
	printf("Escribe la potencia a la que lo desea elevar: ");
	scanf("%d", &p);
	e = pow(n, p);
	printf("%d elevado a la %d es %d \n", n, p, e);
	return 0;
}
