# Majority Element
###### C++ 11

### 1. Approch to solving the problem

Take an array of same type elements and organize them in a map of what the element is and the count of the element. Once organized, iterate through the map to find the element with the count > n/2.

### 2. How to compile and run this

In Windows - I used the Visual Studio C++ compiler, move to the proper directory and run:

```
cl.exe /EHsc src/MajorityElement.cpp
MajorityElement.exe
```

### 3. How this program works

Read the hard coded array, organize the array into a map and count the number of time the element shows up, then display the element that shows up the most.
