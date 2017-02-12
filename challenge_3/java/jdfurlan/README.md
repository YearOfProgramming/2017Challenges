# MajorityElement
###### Java 8

### 1. Approach to Solving the problem

I used a map to make sure all equivalent elements were mapped to the same key
and tracked their frequencies with their value

### 2. How to compile and run this code

Compile the Node class first

```
javac MajorityElement.java
java MajorityElement
```

### 3. How this program works

As we iterate through the list, if the map has never seen this element before,
place it in the map and initialize its frequency at 1. If we have seen it before, increment 
its frequency, check if > n.length/2  and print if true, else update the frequency.
