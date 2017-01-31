# ReverseAString
###### Java 8

### 1. Approach to Solving the problem

Don't use built-in methods, just primitives and arrays

### 2. How to compile and run this code

```
javac ReverseAString.java
java ReverseAString
```

### 3. How this program works

Takes user input and converts to a character array
Track first and last values, store one in a temp variable, then swap
increment and decrement the positions and continue to swap. 
For odd length strings it just leaves the middle value in place, since no swap needed
