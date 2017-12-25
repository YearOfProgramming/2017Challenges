CC     = gcc
CFLAGS = -O3 -Wall -std=c99
SRCDIR = src
OUTPUT = GetSequences
RM     = rm -rf


all: $(SRCDIR)/main.c
	$(CC) $(CFLAGS) -o $(OUTPUT) $(SRCDIR)/*.c

clean:
	$(RM) $(OUTPUT)

test:
	@./$(OUTPUT) 1 2 3 4 8 9 10 12 13 14
	@./$(OUTPUT) 1 2 3 4 9 10 15
