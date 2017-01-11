# Single Number

### 1. Approch to Solving the problem

My approach to solving this problem is to first find the max number 
in the given set of numbers

Once I have the max numbers, I create a counting array of the l
ength of the max numbers with all the values set to 0;

I then iterate through the set of numbers and increment the value of
each index of the count array for each value of the set of numbers

Example:
Given a set of numbers: 1,2,2,7,7

I create a count array of size 7 with all 0s: [0, 0, 0, 0, 0, 0, 0]

As I iterate through those numbers i increment the matching index value
for that number in the count array.

The index that contains a value of 1 is the single number.

### 2. How to compile this code

Assuming you are within the directory under my name

```
$ make
```

### 3. How this program works

This program takes in an array as as a line of standard input and outputs the single number

