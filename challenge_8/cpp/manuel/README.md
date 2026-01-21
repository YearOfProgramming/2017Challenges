# Random Pointer Linked List
###### C++11 @manuel

### 1. Approch to Solving the problem

I assume that I am given a linked list that is prebuilt and the random
attribute always points to a random node, so I do not verify whether the 
connections match.

To make copies I map every node in the given list with a copy.

I then iterate through my linked list and assign every attribute in
the copy to the corresponding copy of the given node.

To test this I make a simple linked list containing all the letters
alphabet and make a copy of it to verify.

### 2. How to compile and run this code

```
make
make clean
```

### 3. How this program works

This program does not take any input data and prints out
the tests I run in the main method.
