#include <stdio.h>
#include <stdlib.h>

struct nodo
{
	struct nodo *hijoizq;
	struct nodo *hijoder;
	int dato;
};

struct nodo *nuevoNodo(int dato)
{
	size_t tam_nodo = sizeof(struct nodo);
	struct nodo *nuevo_nodo = (struct nodo *)malloc(tam_nodo);
	nuevo_nodo->dato = dato;
	nuevo_nodo->hijoizq = NULL;
	nuevo_nodo->hijoder = NULL;
	return nuevo_nodo;
}

void insertarNodo(struct nodo *nd, int dato)
{
	if (dato < nd->dato)
	{
		if (nd->hijoder == NULL)
		{
			nd->hijoder = nuevoNodo(dato);
		}
		else
		{
			insertarNodo(nd->hijoder, dato);
		}
	}
	else
	{
		if (nd->hijoizq == NULL)
		{
			nd->hijoizq = nuevoNodo(dato);
		}
		else
		{
			insertarNodo(nd->hijoizq, dato);
		}
	}
}
int where(struct nodo *nd, int dato, int nivel)
{
	if (nd == NULL)
		return 0;
	if (nd->dato == dato)
		return nivel;
	int nuevo_nivel = where(nd->hijoizq, dato, nivel + 1);
	if (nuevo_nivel != 0)
		return nuevo_nivel;
	nuevo_nivel = where(nd->hijoder, dato, nivel + 1);
}

int busqueda(struct nodo *nd, int dato)
{
	return where(nd, dato, 1);
}

int main()
{
	int ra = 0, nn = 0, nr = 0;
	struct nodo *raiz = NULL;
	printf("Ingresa la raiz del arbol: ");
	scanf("%d", &ra);
	raiz = nuevoNodo(ra);
	printf("cuantos numeros desea ingresar a el arbol? ");
	scanf("%d", &nn);
	for (int i = 0; i <= nn; i++)
	{
		printf("Ingrese el %d numero: ", i);
		scanf("%d", &nr);
		insertarNodo(raiz, nr);
	}
	int x;
	do
	{
		printf("\nIngresa el numero que desea buscar: ");
		scanf("%d", &x);
		if (x != 9999)
		{
			int nivel = busqueda(raiz, x);
			if (nivel)
			{
				printf("El numero %d esta en en nivel %d\n", x, busqueda(raiz, x));
			}
			else
			{
				printf("El numero que estas buscando no esta en el arbol\n");
			}
		}
		printf("Desea buscar otro numero? (0=Si, 999=No): ");
		scanf("%d", &x);
	} while (x != 999);
	printf("\n Que tengas un buen dia! \n");
	return 0;
}