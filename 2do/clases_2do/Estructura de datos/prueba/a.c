#include <stdio.h>
#include <math.h>

int exponen(int n, int p){
        if(p==0){
            return 1;
        } else if (p<0) {
            return exponen(n, p+1) / n;
        } else {
            return n * exponen(n, p-1);
        }
    }
     
void main() {
      	int n, p;
        printf("Ingresa el numero: ");
        scanf("%d", &n);
        printf("Escribe la potencia a la que lo desea elevar: ");
        scanf("%d", &p);
	printf("%d elevado a %d es igual a %d  \n", n, p, exponen(n, p));
}
