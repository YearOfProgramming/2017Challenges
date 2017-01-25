# Ranges
###### Java 8

### 1. Approach to Solving the problem

I thought about various ways to compare values in a string.
Using a boolean array is a common solution for comparing characters.

### 2. How to compile and run this code


```
javac Ranges.java
java Ranges
```

### 3. How this program works

Create a boolean array of size 128, the ASCII code limit
(this program wouldn't work for Unicode, too many chars)
Every char value maps to an index in the array, walk through string
s and put each boolean at the char index to true. Then walk through string
t and as soon as you reach a boolean that is false, we know that's our missing char!
