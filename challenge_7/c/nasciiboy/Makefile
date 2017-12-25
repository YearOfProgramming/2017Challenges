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
	@echo
	@./$(OUTPUT) -7 -6 -5 -4 -2 -1 0 1 2
	@echo
	@./$(OUTPUT) 10 11 12 13 14 16
	@echo
	@./$(OUTPUT) 777 778 779 781 782 783
	@echo
	@./$(OUTPUT) -777 -778 -779 -781 -782 -783
