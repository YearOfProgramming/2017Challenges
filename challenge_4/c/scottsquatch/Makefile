SRCDIR=src
OUTDIR=bin
APPNAME=binary_tree_reverse
RM=rm -rf
TESTDIR=test
CFLAGS=-I -g -Wall -I src
CC=gcc
DEPS=binary_tree.h

$(OUTDIR)/binary_tree.o : $(SRCDIR)/binary_tree.h
	$(CC) $(CFLAGS) -c -o $(OUTDIR)/binary_tree.o $(SRCDIR)/binary_tree.h

$(OUTDIR)/binary_tree_tests.o : $(TESTDIR)/binary_tree_tests.c
	$(CC) $(CFLAGS) -c -o $(OUTDIR)/binary_tree_tests.o $(TESTDIR)/binary_tree_tests.c

test: $(OUTDIR)/binary_tree.o $(OUTDIR)/binary_tree_tests.o
	$(CC) $(CFLAS) -o $(OUTDIR)/binary_tree_tests $(OUTDIR)/binary_tree.o $(OUTDIR)/binary_tree_tests.o
	./$(OUTDIR)/binary_tree_tests

clean:
	$(RM) $(OUTDIR)/*
