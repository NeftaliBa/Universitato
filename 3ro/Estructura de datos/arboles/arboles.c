#include <stdio.h>
#include <stdlib.h>

struct nodo{
	struct nodo *hijoizq;
	struct nodo *hijoder;
	int dato;
};

struct nodo *nuevoNodo(int dato){
	size_t tam_nodo = sizeof(struct nodo);
	struct nodo *nuevo_nodo = (struct nodo *)malloc(tam_nodo);
	nuevo_nodo->dato = dato;
	nuevo_nodo->hijoizq = NULL;
	nuevo_nodo->hijoder = NULL;
	return nuevo_nodo;
}

void insertarNodo(struct nodo *nd, int dato){
	if (dato < nd->dato){
		if (nd->hijoder == NULL){
			nd->hijoder = nuevoNodo(dato);
		}
		else{
			insertarNodo(nd->hijoder, dato);
		}
	} else {
		if (nd->hijoizq == NULL){
			nd->hijoizq = nuevoNodo(dato);
		} else {
			insertarNodo(nd->hijoizq, dato);
		}
	}
}
int main(){
	struct nodo *raiz = NULL;
	raiz = nuevoNodo(8);
	insertarNodo(raiz, 3);
	insertarNodo(raiz, 20);
	return 0;
}
