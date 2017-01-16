# Challenge_0
###### C compiled with gcc 4.2.1

### 1. Approch to Solving the problem

This one is pretty straight forward.  You jut have to understand what standard library
and standard library function will be used to print something out to the command line --
printf() was used here.  Tons of print options exist depending on what type of file
you want to print to ( printf, fprintf, sprintf, snprintf, asprintf, dprintf, vprintf, 
vfprintf, vsprintf, vsnprintf, vasprintf, vdprintf).  I wanted to print to standard out
so printf() was used.
 
### 2. How to compile and run this code

Make sure that you have gcc installed on your *nix machine.  To see if you have
it installed you can type:

```
$ gcc --version
``` 

Compiling:
```
$ gcc -o challenge0 challenge0.c
```
Or optionally with symbols that aid in debugging, not that you'd
need that for a hello world...
```
$ gcc -g -o challenge0 challenge0.c
```

### 3. How this program works

After the program has compiled with no errors:
```
$ ./challenge0
Hello world!

```
