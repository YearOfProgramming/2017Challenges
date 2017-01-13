# Compression and Decompression 1
###### Java 8

### 1. Approach to Solving the problem

My first approach involved tracking the count of equal characters found in a row
and once characters changed, checking the number of equal characters and compressing if over the threshold

### 2. How to compile and run this code

```
javac CompAndDecompOne.java
java CompAndDecompOne
```

### 3. How this program works

Walk through strings and compress based on the threshold. Decompress based 
on integer value of character used during compression.