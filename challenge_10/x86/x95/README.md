#Checking Brackets in x86-Assembly (64-Bit)

##Contents
brackets.s contains the main fuction check_brackets checks the input for correct formatting.

The caller to the function only needs to provide the String.
##Compiling
```
$ as brackets.s -o brackets.o
$ gcc -m64 challenge10.c brackets.o -o c10
```
tested on Ubuntu 16.04 64-Bit
##Testing
To test the implementation just start the c10 application and type the testcases in.

The C file will call the asm function. Please take note, that this ASM file follows the AMD64 calling convention and not the Microsoft calling convention. Therefore it can only work on Linux/OSX/*NIX.
