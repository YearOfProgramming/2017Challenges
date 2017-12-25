CC      = gcc
CCFLAGS = -Wall -std=c99
SRCDIR  = src
OUTPUT  = InvertBinaryTree
RM      = rm -rf

all: $(SRCDIR)/main.c
	$(CC) $(CCFLAGS) -o $(OUTPUT) $(SRCDIR)/*.c

clean:
	$(RM) $(OUTPUT)

test:
	@./$(OUTPUT) 4 2 1 3 7 6 9
