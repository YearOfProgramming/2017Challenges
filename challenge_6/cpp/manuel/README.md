# Challenge Name
###### C++11

### 1. Approch to Solving the problem

Set start of range as first index of number array.
Set end of range as first index of number array.

Iterate through numbers.

If there's a gap of 1 or greater between the current end of range
and the next number and start does not equal end, then we have a range.

Otherwise, if there's a gap of 1 or greater between the current end
of range, and start is equal to end, then we have an isolated number
and we can skip it.

Set end of range as next index

### 2. How to compile and run this code

This will run the executable through the test script

```
make
make test
make clean
```

### 3. How this program works

Expects a line: 
    
    1,2,4,5,6

Outputs:

    1->2
    4->6

