# Invert Binary Tree
###### C++ 11

### 1. Approch to solving the problem

Make the Binary tree with all the functions of printing, creating nodes and deleting the tree. Also include the actual function we are looking for, that inverts the tree. Create a temp node that points to the left child, make the left child point to the right child, then make the right child point to the left child. The call is then placed recursively in order to fully inverse the tree.

### 2. How to compile and run this

In Windows - I used the Visual Studio C++ compiler, move to the proper directory and run:

```
cl.exe /EHsc src/InvertBT.cpp src/BinaryTree.cpp
InvertBT.exe
```

### 3. How this program works

You build the tree how you want it to look, via create node. Once complete you then use the InverseTree function to inverse the tree, then print it out. Warning: this does not make a new tree, it uses the original data. 
