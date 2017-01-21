# Challenge_2
###### C compiled with gcc 4.2.1

### 1. Approch to Solving the problem

We assume that we know the list has numbers which only
occur once.  From that assumption, you could go through the
list and count how many instances of a particular number there are and then return that.
However, I wanted to do this more generally and did so
inside inside of a nested for loop.  The outer loop
goes through the array and the inner loop checks of that number
occurs multiple times.  If it only occurs once, it is unique
and will be the answer.

### 2. How to compile and run this code

Make sure that you have gcc installed on your *nix machine.  To see if you have
it installed you can type:

```
$ gcc --version
```

Compiling:
```
$ gcc -o challenge2 challenge2.c
```
Or optionally with symbols that aid in debugging.
```
$ gcc -g -o challenge2 challenge2.c
```

### 3. How this program works

After the program has compiled with no errors:
```
$ ./challenge2
5

```
