# Challenge Name
###### C++11 @manuel

### 1. Approch to Solving the problem

Given a set of numbers ranging from 0 to N-1 with one missing number,
then the largest number in that set is the length of the array. 

If we find the sum of N + (N-1) + (N - 2) + ... + (N - N) = N * (N + 1) / 2,
and then iterate through the given set and subtract this value, once we
reach the end of the array the difference will be the missing number.

### 2. How to compile and run this code

```
make
make test 
make clean
```

### 3. How this program works

Single line of input -> Single line of output
             1,3,4,0 -> 2 
