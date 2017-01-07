#Reversing a String in x86 Assembly (64-Bit)

##Contents
reversestring.s includes the main fuctions reverse_string and calc_msglen, which are used for reversing the string.

The caller to the function needs to provide the string and the buffer for the output. An example call is included.
##Compiling
```
$ as reversestring.s -o reversestring.o
$ ld reversestring.o -o reversestring
```
tested on Ubuntu 16.04 64-Bit
