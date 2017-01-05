CC     = gcc
CFLAGS = -O3 -Wall -std=c11
SRCDIR = src
OUTDIR = bin
OUTPUT = unintq
RM     = rm -rf



all: $(SRCDIR)/main.c
	@mkdir -p $(OUTDIR)
	$(CC) $(CFLAGS) -o $(OUTDIR)/$(OUTPUT) $(SRCDIR)/*.c

clean:
	$(RM) $(OUTDIR)/*

test:
	@$(OUTDIR)/$(OUTPUT)
