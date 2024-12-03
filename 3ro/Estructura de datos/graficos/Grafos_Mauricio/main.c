#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
#include<SDL2/SDL.h>
#include<cairo/cairo.h>

#define SPACE 50
#define RADIUS 20
int WIDTH = 0;
int HEIGHT = 0;
cairo_t *ctx = NULL;

// Estructura del nodo
struct node {
	struct node *left;
	struct node *right;
	int data;
	int x; int y;
	int lvl;
};

struct node* new_node(int data, int lvl, int x, int y);
void insert_node(struct node* node, int data);
char* itoa(int i);

int main(){
	//variables
	bool running = true;
	SDL_Renderer *renderer;
	SDL_Window *window;
	SDL_Texture *image;

	//comprobaciones
	if (SDL_Init(0) != 0){
		printf("Error iniciando SDL: %s", SDL_GetError());
		exit(EXIT_FAILURE);
	}
	if(SDL_CreateWindowAndRenderer(WIDTH, HEIGHT, SDL_WINDOW_FULLSCREEN, &window, &renderer) != 0){
		printf("Error creando recursos de SDL: %s", SDL_GetError());
		exit(EXIT_FAILURE);
	}
	SDL_GetWindowSize(window, &WIDTH, &HEIGHT);
	SDL_Surface *surface = SDL_CreateRGBSurface(
		0,
		WIDTH,
		HEIGHT,
		32,
		0x00ff0000,
		0x0000ff00,
		0x000000ff,
		0xff000000);

	if(surface == NULL){
		printf("No se pudo crear la superficie: %s", SDL_GetError());
		exit(EXIT_FAILURE);
	}

	//Creando imagen
	cairo_surface_t *csf = cairo_image_surface_create_for_data(
		surface->pixels,
		CAIRO_FORMAT_ARGB32,
		WIDTH,
		HEIGHT,
		surface->pitch
	);

	ctx = cairo_create(csf);
	cairo_select_font_face(ctx, "monospace",
     CAIRO_FONT_SLANT_NORMAL,
     CAIRO_FONT_WEIGHT_BOLD);
	cairo_set_font_size(ctx, 18);
	struct node* root = new_node(10, 1, WIDTH / 2, SPACE);
	insert_node(root, 15);
	insert_node(root, 5);
	insert_node(root, 3);
	insert_node(root, 6);
	insert_node(root, 17);
	insert_node(root, 13);
	insert_node(root, 21);
	image = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_FreeSurface(surface);
	cairo_destroy(ctx);
	cairo_surface_destroy(csf);
	SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
	SDL_RenderClear(renderer);
	SDL_RenderCopy(renderer, image, NULL, NULL);
	SDL_RenderPresent(renderer);
	while(running){
		SDL_Event e;
		SDL_WaitEvent(&e);
		if(e.type == SDL_QUIT)
			running = false;
	}
	SDL_DestroyTexture(image);
	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
	SDL_Quit();
	return 0;
}

struct node* new_node(int data, int lvl, int x, int y) {
	struct node *new = malloc(sizeof(struct node));
	new->left = NULL;
	new->right = NULL;
	new->data = data;
	new->x = x;
	new->y = y;
	new->lvl = lvl;
	cairo_set_source_rgb(ctx, 0, 0, 0);
	cairo_arc(ctx, x, y, RADIUS, 0, M_PI * 2);
	cairo_fill(ctx);
	cairo_set_source_rgb(ctx, 1, 1, 1);
	cairo_move_to(ctx, x, y);
	char* n = itoa(new->data);
  cairo_show_text(ctx, n);
	free(n);
	return new;
}

void insert_node(struct node* node, int data) {
	if (data < node->data) {
		if (node->left == NULL) {
			node->left = new_node(
					data, node->lvl + 1, 
					node->x - (WIDTH >> (node->lvl + 1)), 
					node->y + SPACE
				);
			cairo_set_source_rgb(ctx, 0, 0, 0);
			cairo_move_to(ctx, node->x, node->y);
			cairo_line_to(ctx, node->left->x, node->left->y);
			cairo_stroke(ctx);
		} else
			insert_node(node->left, data);
	} else {
		if (node->right == NULL) {
			node->right = new_node(
					data, node->lvl + 1, 
					node->x + (WIDTH >> (node->lvl + 1)),
					node->y + SPACE
					);
			cairo_set_source_rgb(ctx, 0, 0, 0);
			cairo_move_to(ctx, node->x, node->y);
			cairo_line_to(ctx, node->right->x, node->right->y);
			cairo_stroke(ctx);
		} else
			insert_node(node->right, data);
	}
}

char* itoa(int i) {
	char* num = NULL;
	int len = 1;
	while (i > 0) {
		len++;
		num = realloc(num, sizeof(char) * len);
		num[len - 2] = '0' + (i % 10);
		i = i / 10;
	}
	num[len - 1] = '\0';
	for (int j = 0; j < (len - 1) / 2; j++) {
		char aux = num[j];
		num[j] = num[len - 2 - j];
		num[len - 2 - j] = aux;
	}
	return num;
}

