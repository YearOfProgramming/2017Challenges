# InvertBinaryTree
###### Java 8

### 1. Approach to Solving the problem

Trees suck if you haven't messed with them in a while!
Swapping the values is relatively easy using an A-B-C swap approach.
The approach to print was to do a [Breadth-First Traversal](https://www.cs.bu.edu/teaching/c/tree/breadth-first/)

### 2. How to compile and run this code

Compile the Node class first

```
javac InvertBinaryTree.java
java InvertBinaryTree
```

### 3. How this program works

Iterate through the array, if the key is new add it and frequency of 1
Otherwise increment its frequency. After incrementing, check if that frequency is > n/2
