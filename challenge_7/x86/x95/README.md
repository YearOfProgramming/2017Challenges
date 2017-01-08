#Finding the missing number in x86 Assembly (64-Bit)

##Contents
missingnumber.s contains the main fuction find_missnumber which finds the missing number in an array.

The caller to the function needs to provide the array (32-bit integers) and the size of the array.
##Compiling
```
$ as --gstabs+ missingnumber.s -o ms.o
$ ld ms.o -o ms
```
tested on Ubuntu 16.04 64-Bit
##Testing
To test the implementation the whole source code was compiled with Gstabs+ support. This enables you to debug the application.
```
$ gdb ./ms
$ (gdb) b 10
$ (gdb) run
$ (gdb) info registers rax
$ (gdb) quit
$ (gdb) y
```

In x86 the result of a function is usually located in the RAX register.

gdb b 10 enables you to set a breakpoint before the Exit(0) Syscall is set up. The result is located in RAX.
