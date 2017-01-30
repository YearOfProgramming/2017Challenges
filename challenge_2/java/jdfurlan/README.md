# SingleNumber
###### Java 8

### 1. Approach to Solving the problem

Maps are usually good for storing unique values since there 
can only be 1 of any given key in a map. A set is also good for this
but since we needed to track the occurence of a key, I decided to use map
and track occurance with the value

### 2. How to compile and run this code

```
javac SingleNumber.java
java SingleNumber
```

### 3. How this program works

If a key doesn't already exist in the map, put it in and set its value to 1
Otherwise, key the value with associated key and increment by 1.
Next, interate through the keySet and check when the value == 1, then return and exit
