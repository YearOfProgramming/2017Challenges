# IntegerPalindrome
###### Java 8

### 1. Approach to Solving the problem

When it comes to breaking numbers down to specific digits, modulus and integer division are usually 
the first things I will look at. Once I realize how to separate a specific digit, I can then
build a new number by using *10 to give a '0 buffer' to add the digit onto.

### 2. How to compile and run this code

```
javac IntegerPalindrome.java
java IntegerPalindrome
```

### 3. How this program works

Get the last digit using %, add that onto a new 'reversed' number with a 
'0 buffer' on it, which is done by * 10. Chop the original down by / 10
and go until it is 0. Compare reversed with original.
