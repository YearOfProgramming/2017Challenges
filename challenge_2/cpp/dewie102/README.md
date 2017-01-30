# Single Number
###### C++ 11

### 1. Approch to solving the problem

Traverse the array, with each number/ character search a map of all previously checked items. If the number/ character is present, increase the count. If it is not then add it to the map. Once complete iterate over the map to find the count that is equal to 1 and output that number/ character.

### 2. How to compile and run this

In Windows - I used the Visual Studio C++ compiler, move to the proper directory and run:

```
cl.exe /EHsc src/SingleNumber.cpp
SingleNumber.exe
```

You can edit the .cpp file and change up the array or change the CountArray parameter to a different array you want to test. You have to rerun the code above to recompile and run the program.

### 3. How this program works

Given the hardcoded array, I stored it as a vector of strings in order to be able to do both numbers and characters. The function stores how many of the same character appears in the array using a map. It then iterates the map searching for the key that has a 1 mapped to it, signifying only one instance.
