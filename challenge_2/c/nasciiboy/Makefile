CC     = gcc
SRCDIR = src
OUTDIR = bin
OUTPUT = unintq
RM     = rm -rf

all: $(SRCDIR)/main.c
	mkdir -p $(OUTDIR)
	$(CC) -g -Wall -o $(OUTDIR)/$(OUTPUT) $(SRCDIR)/*.c

clean:
	$(RM) $(OUTDIR)/*

test:
	@$(OUTDIR)/$(OUTPUT)
