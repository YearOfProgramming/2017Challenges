#Inverting a Binary Tree in x86-Assembly (64-Bit)

##Contents
invertTree.s contains the main fuction invertTree which inverts the input tree.

The caller to the function only needs to provide the address to the root.
##Compiling
```
$ as invertTree.s -o invertTree.o
$ gcc -m64 challenge4.c invertTree.o -o c4
```
tested on Ubuntu 16.04 64-Bit
##Testing
To test the implementation just start the c4 application.

It will recreate the tree from the challenge and then traverse it in post-order. Then the ASM function will invert the tree. To check the result, the application will traverse the tree in post-order yet again.
