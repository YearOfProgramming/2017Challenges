SRCDIR=src
OUTDIR=bin
APPNAME=reverse_string
RM=rm -rf

all: $(SRCDIR)/*
	mkdir -p $(OUTDIR)
	gcc -g -Wall -o $(OUTDIR)/$(APPNAME) $(SRCDIR)/*

clean:
	$(RM) $(OUTDIR)/*
