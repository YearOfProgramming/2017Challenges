CC     = gcc
SRCDIR = src
OUTDIR = bin
OUTPUT = helloWorld
RM     = rm -rf

all: $(SRCDIR)/main.c
	mkdir -p $(OUTDIR)
	$(CC) -g -Wall -o $(OUTDIR)/$(OUTPUT) $(SRCDIR)/*.c

clean:
	$(RM) $(OUTDIR)/*

test:
	@$(OUTDIR)/$(OUTPUT)
