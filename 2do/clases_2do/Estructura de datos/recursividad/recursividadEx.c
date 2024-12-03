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
        double n, p;
        printf("Introduce un numero y su potencia: \n");
	scanf("%lf %lf", &n, &p);
        printf("%.0lf elevado a %.0lf es igual: %d  \n", n, p, exponen(n, p));
}

