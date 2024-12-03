#include <stdio.h>

int main (){
	 double num1, num2, tmp;
	 double *ptr1, *ptr2;

	 ptr1 = &num1;
	 ptr2 = &num2;

	 num1 = 10;
	 num2 = 20;

	 printf("num1: %ld, num2: %ld \n\n", num1, num2);

	 tmp =  *ptr1;
	 *ptr1 = *ptr2;
	 *ptr2 = tmp;

	 printf("ptr1: %ld, ptr2: %ld \n\n", &ptr1, &ptr2);
	 
	 return 0;
}
