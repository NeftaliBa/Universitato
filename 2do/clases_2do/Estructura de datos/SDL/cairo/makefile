CC = gcc
LIBS= `pkg-config cairo sdl2 --libs --cflags`
MAIN = main.c
OUT = first_cairo

build:
	$(CC) $(LIBS) $(MAIN) -o $(OUT) 

run:
	./$(OUT)
	
clean: 
	rm $(OUT)
