# Invert Binary Tree

### 1. Approch to Solving the problem

Given an array of integers in the form: [1,2,3,4,5,6]

The tree would would be build such that:

The left child of the current node is 2 * (current index) + 1
The right child of the current node is 2 * (current index) + 2

Starting at index 0 is the root. So it's left child is 2 * 0 + 1, 
which is 1. It's right child is 2 * 0 + 2, which is 3. The left child
of index 1, is 2 * 1 + 1, which is index 3. The right child of index 1
is 2 * 1 + 2. And so on.

```
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
```
Pre Order Traversal of this tree would print out: 

```
1
2
4
5
3
6
7
```


### 2. How to compile this code

Assuming you are within the directory under my name

```
$ g++ src/main.cpp src/treeInversion.cpp -o challenge_4.exe
$ ./challenge_4.exe < src/input
```

### 3. How this program works

I have a file in the src/ directory that you can modify. 
The first line is the number of testcases to test and following
that each line is a testcase.


