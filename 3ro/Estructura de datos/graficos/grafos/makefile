CC = gcc
FILE = main.c
OUTPUT = cairo
LIBS = `pkg-config --cflags --libs sdl2 cairo`

run: build
	./$(OUTPUT)

build:
	$(CC) $(FILE) -o $(OUTPUT) $(LIBS)

clean:
	rm $(OUTPUT)