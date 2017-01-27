# Challenge_1
###### C compiled with gcc 4.2.1

### 1. Approch to Solving the problem

Reversing strings in C is a little bit more challenging than
higher level languages.  Since basically everything is a pointer
to memory of a particular size, you must make sure that the variables
you're creating have the approprate space.  In short, I created two
character arrays and looped through them from opposite directions,
the original's end filling the beginning of the reverse string.

### 2. How to compile and run this code

Make sure that you have gcc installed on your *nix machine.  To see if you have
it installed you can type:

```
$ gcc --version
```

Compiling:
```
$ gcc -o challenge1 challenge1.c
```
Or optionally with symbols that aid in debugging.
```
$ gcc -g -o challenge0 challenge0.c
```

### 3. How this program works

After the program has compiled with no errors:
```
$ ./challenge1
olleH

```
