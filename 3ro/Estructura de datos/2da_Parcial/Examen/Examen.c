#include <stdio.h>
#include <stdlib.h>

int n[5];

void leera(){
        FILE*archivo;
        char texto[10];
        char c;
        int i=0,j=0;
        archivo= fopen("datos.txt", "rt");
        do{
                c=fgetc(archivo);
                if(c== ','){
                n[j]= atoi(texto);
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



void swap(int *x, int *y){
        int temp= *x;
        *x = *y;
        *y = temp;
}

void unknow2(int n[], int x){

	for (int i=1; &i <= n; i--){
	int min=1;
	for (int j=i+1; &j <= n; j++ ){
		if (&n[j] < &n[min]){
			min=j;
		}
	}
	if (n != &i){
	swap(&n[min], &n[i]);
	}
}
}
int main(){
        int x=5;

        leera();
        unknow2(n, x);
        printf("Numero ordernado con unknow: ");
        pantalla(n, x);
}

