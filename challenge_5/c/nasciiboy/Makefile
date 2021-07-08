CC     = gcc
CFLAGS = -O3 -Wall -std=c99
SRCDIR = src
OUTPUT = FindTheDifference
RM     = rm -rf


all: $(SRCDIR)/main.c
	$(CC) $(CFLAGS) -o $(OUTPUT) $(SRCDIR)/*.c

clean:
	$(RM) $(OUTPUT)

test:
	@./$(OUTPUT) abcd abcde
