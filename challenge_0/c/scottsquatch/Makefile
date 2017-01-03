SRCDIR=src
OUTDIR=bin
APPNAME=helloworld
RM=rm -rf

all: $(SRCDIR)/main.c
	mkdir -p $(OUTDIR)
	gcc -g -Wall -o $(OUTDIR)/$(APPNAME) $(SRCDIR)/*

clean:
	$(RM) $(OUTDIR)/*
