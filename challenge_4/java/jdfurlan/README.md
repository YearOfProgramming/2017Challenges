# InvertBinaryTree
###### Java 8

### 1. Approach to Solving the problem

Trees suck if you haven't messed with them in a while!
Swapping the values is relatively easy using an A-B-C swap approach.
The approach to print was to do a [Breadth-First Traversal](https://www.cs.bu.edu/teaching/c/tree/breadth-first/)

### 2. How to compile and run this code


```
javac InvertBinaryTree.java
java InvertBinaryTree
```

### 3. How this program works

Hand the root node to the swap function. There, while the node is not null
you must take either child and store in a temp, then swap into the other child's place
then swap the child you didn't store into a temp with the temp child.
Call the swap function recursively with either child first, then the other child.
BFT through the tree to print values by level.
