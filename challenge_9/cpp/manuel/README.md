# Squares
###### C++11 @manuel

### 1. Approach to Solving the problem

First I iterate through the given set of numbers and square all 
the negative until I reach the numbers that are greater than or
equal to 0. 

At this point I have the length of the left side of the array, 
and I know the right side by subtracting the length of the 
given set minus the length of the left side.

I then square the first index of the right side and compare to the 
last index of the left side of the array, and insert the smallest 
one into a new array. 

I then either decrement or increment depending on which one
was smaller. 

This will sort all the values in one pass, or slightly greater.

### 2. How to compile and run this code

```
make
make test 
make clean
```

### 3. How this program works

Single line of input:

    -1,0,-1,2,3

Output:

    0
    1
    1
    4
    9
