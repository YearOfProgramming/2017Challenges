SRCDIR=src
OUTDIR=bin
APPNAME=majority_element
RM=rm -rf

all: $(SRCDIR)/*
	mkdir -p $(OUTDIR)
	gcc -g -Wall -o $(OUTDIR)/$(APPNAME) $(SRCDIR)/*

clean:
	$(RM) $(OUTDIR)/*
