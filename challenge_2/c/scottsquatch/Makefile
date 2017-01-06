SRCDIR=src
OUTDIR=bin
APPNAME=find_non_dups
RM=rm -rf

all: $(SRCDIR)/*
	mkdir -p $(OUTDIR)
	gcc -g -Wall -o $(OUTDIR)/$(APPNAME) $(SRCDIR)/*

clean:
	$(RM) $(OUTDIR)/*
