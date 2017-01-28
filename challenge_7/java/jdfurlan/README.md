# Find the Missing Number
###### Java 8

### 1. Approach to Solving the problem

I kept thinking about using different data structures which really annoying me!
I then though about the relationship between what the actual array would look like
without the missig number, and that's when I realized the only thing separating them
would be the sum of their values!

### 2. How to compile and run this code

```
javac FindTheMissingNumber.java
java FindTheMissingNumber
```

### 3. How this program works

Use "i" to track the incremental sum as if no values were missing. Then use
the same "i" to sum the index values of the array given. Compare the differences
and that's the missing number!