#include <stdio.h>
#include <stdlib.h>

int a[6];

void intercambio(int *x, int *y){
	int temp= *x;
	*x = *y;
	*y = temp;
}

int particion(int a[], int izq, int der){
	int pivote = a[izq];
	while(1){
		while(a[izq] < pivote){
		izq++;
	}
		while(a[der] > pivote){
		der--;
			
	}
			
		if(izq >= der){
			return der;
			
		}else{
			intercambio(&a[izq], &a[der]);
			izq++;
			der--;
		}
	}
}

void quicksort(int a[], int izq, int der){
 if(izq < der ){
 int indice_de_particion = particion(a, izq, der);
 quicksort(a, izq, indice_de_particion);
 quicksort(a, indice_de_particion+1, der);
 }
}

int unknow (int a[], int n){
	for (int i=1; i < n; i++){
		for (int j=i+1; j < n; j++){
		if (a[i]>a[j])
			intercambio(&a[j], &a[j]);
		}
	}
}



int insertion_sort(int a[], int n){
	for (int i = 1; i < n; i++){
		int key = a[i];
		int j = i - 1;
		while (key < a[j] && j >= 0){
			a[j + 1] = a[j];
			--j;
		}
		a[j + 1] = key;
	}
}

void bubble_sort(int a[], int n){	
	for (int i = 1; i < n; i++)
	{	for (int j = 0; j < n - 1; j++)
		{	if (a[j] > a[j + 1]){
				intercambio(&a[j], &a[j+1]);
//				int temp = a[j];
//				a[j] = a[j + 1];
//				a[j + 1] = temp;
// lo deje para recordar
			}
		}
	}
}


void leera(){
	FILE*archivo;
	char texto[20];
	char c;
	int i=0,j=0;
	archivo= fopen("datos.txt", "rt");
	do{
		c=fgetc(archivo);
		if(c== ','){
		a[j]= atoi(texto);
		j++;
		for (int z=0; z<i; z++)
			texto[z]=6;
		i=0;
		continue;
		}
		texto[i]=c;
		i++;
	}while(c!=EOF);
}


void pantalla(int a[], int n){
	for (int j = 0; j < n - 1; j++)
	{
		printf("%d, ", a[j]);
	}
	printf("%d\n", a[n - 1]);
}

int main(){
	int x=6;
//	printf("ingrese la cantidad de numeros a ingresar: ");
//	scanf("%d", &cdn);
	
//	for (x = 0; x < cdn; x++)
//	{
//		printf("ingrese numero %d: ", x + 1);
//		scanf("%d", &a[x]);
//	}
	
	leera();


	printf("Numero ingresado: ");
	pantalla(a, x);
	
	//bubble
	bubble_sort(a, x);
	printf("numero ordenado con bubble: ");
	pantalla(a, x);

        //unknow
        unknow(a, x);
	printf("numero ordenado con unknow: ");
	pantalla(a, x); 

	//insertion
	insertion_sort(a, x);
	printf("numero ordenado con insertion: ");
	pantalla(a, x);

	//quicksort
	quicksort(a, x+1, x);
	printf("numero ordernado con quicksort: ");
	pantalla(a, x);
	

	int num=0;
	int pos=0;
	

	while(1){
	//busqueda de valor
	printf("Ingrese el numero que desea buscar: ");
	scanf("%d", &num);
	if(num ==-1) break;


	for (int i=0; i < a[i]; i++){
		pos= i;
		break;
	} pos =-1;
   }
	if(pos != -1){
		printf("%d esta en la posisicion %d del arreglo \n", num, pos);
	} else {
		printf("%d no existe en el arreglo \n", num);
	}

}
