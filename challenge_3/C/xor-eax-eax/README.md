# Challenge_3
###### C compiled with gcc 4.2.1

### 1. Approch to Solving the problem

The problem called for the commandline to pass in a
finite sized, comma-delimited string of ints.
I took the argv[1] information and used the strtok
function with the comma as a delimter to create
substrings which populated a fixed size array.

I then passed this to a function which counted
a particular value against all others to see how many
instances of the number there were.  If it was more than
n/2 where n is the number of elements in the array,

### 2. How to compile and run this code

Make sure that you have gcc installed on your *nix machine.  To see if you have
it installed you can type:

```
$ gcc --version
```

Compiling:
```
$ gcc -o challenge3 challenge3.c
```
Or optionally with symbols that aid in debugging.
```
$ gcc -g -o challenge3 challenge3.c
```

### 3. How this program works

After the program has compiled with no errors:
```
$ ./challenge3 2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7
7

```
