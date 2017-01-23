CC     = gcc
CFLAGS = -O3 -Wall -std=c99
SRCDIR = src
OUTPUT = findMissing
RM     = rm -rf


all: $(SRCDIR)/main.c
	$(CC) $(CFLAGS) -o $(OUTPUT) $(SRCDIR)/*.c

clean:
	$(RM) $(OUTPUT)

test:
	@./$(OUTPUT) 1 2 3
	@echo
	@./$(OUTPUT) 1 3 4 0
	@echo
	@./$(OUTPUT) 1 3 4 6 2
	@echo
	@./$(OUTPUT) -1 -2 0 -4 1 2
