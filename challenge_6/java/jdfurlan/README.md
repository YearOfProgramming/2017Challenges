# Ranges
###### Java 8

### 1. Approach to Solving the problem

I very much didn't want to use any additional data structures to help
with traversing the array, and wanted to keep it as is. The reason an 
array list is used is simply because I needed a dynamicly sized array 
since there's no way to know beforehand how many ranges we will find.

### 2. How to compile and run this code

```
javac Ranges.java
java Ranges
```

### 3. How this program works

Assuming we have at least 2 values, we initialize the first range point
as the first value, and the last to 0. We then check that the next value is
equal to the first + 1, meaning incremental. If true, keep incrementing and 
setting the last range point to the current value. To handle index out of bounds
I just break out of the loop when i == the length of the array - 1. The final check
is if last = 0, we know it was never updated and we have array of size 2 but the second
value isn't incremental from the first, so return empty list.
