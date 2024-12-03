#include <stdio.h>

int fibo_recur(int n){
 //Fibonacci Recursivo
 if(n==0){
	 return 0;
 }else if (n==1){
	return 1;
 }else{
 return (fibo_recur(n-1) + fibo_recur(n-2));
 }
}

int fibo_iter(int n){
 //fibonacci Iterativo
 int a=0, b=1, f=0; //0,1,2,3,4,5,8,13,21
for (int i=0; i<=n; i++){
 f=a+b;
 a=b;
 b=f;
 }
 return a;
}

void main (){
	int n=0;
	printf("Ingresa el numero de iteraciones: ");
	scanf("%d", &n);

	for(int i=0; i<=n; i++){
	printf("%d \n", fibo_iter(i));
	}
	//fibo_iter(it);
}

