#include <stdio.h>
#include <stdlib.h>

int n[5];

void swap(int *x, int *y)
{
        int temp = *x;
        *x = *y;
        *y = temp;
}

int particion(int a[], int izq, int der)
{
        int pivote = a[izq];
        while (1)
        {
                while (a[izq] < pivote)
                {
                        izq++;
                }
                while (a[der] > pivote)
                {
                        der--;
                }
                if (izq >= der)
                {
                        return der;
                }
                else
                {
                        swap(&a[izq], &a[der]);
                        izq++;
                        der--;
                }
        }
}

void leera()
{
        FILE *archivo;
        char texto[10];
        char c;
        int i = 0, j = 0;
        archivo = fopen("datos.txt", "rt");
        do
        {
                c = fgetc(archivo);
                if (c == ',')
                {
                        n[j] = atoi(texto);
                        j++;
                        for (int z = 0; z < i; z++)
                                texto[z] = 6;
                        i = 0;
                        continue;
                }
                texto[i] = c;
                i++;
        } while (c != EOF);
}

void pantalla(int a[], int n)
{
        for (int j = 0; j < n - 1; j++)
        {
                printf("%d, ", a[j]);
        }
        printf("%d\n", a[n - 1]);
}

void unknow2(int list[], int n)
{
        int min = 0;
        for (int i = 0; i < n; i++)
        {
                min = i;
                for (int j = i + 1; j < n; j++)
                {
                        if (list[j] < list[min])
                        {
                                min = j;
                        }
                }
                if (min != i)
                {
                        swap(&list[min], &list[i]);
                }
        }
}
int main()
{
        int x = 5;

        leera();
        unknow2(n, x);
        printf("Numero ordernado con unknow: ");
        pantalla(n, x);
}