# Challenge #7 - Missing Number
###### Python 3.5.2

### 0. Problem Statement

##### Premise
  * Given a list of n-1 integers between 0 and n find the missing integer.
    
##### Input Format

  * Assume the input will be a non empty
  * The list will NOT always be ordered.
  * The list will only contain integers.
  * You cannot sort the list (sorting is expensive)
  * Limited resources 
    * O(1) Space 
    * O(n) Complexity

 
---

### 1. Approach to Solving the problem

I'll admit I had no idea how to do this without sorting and had to resort to google fu to find the answer.
 
 This solution takes the sum `(n * (n+1) / 2)` of n numbers and subtracts the sum of the given numbers to find the missing number from the set.
  
 
---

### 2. How to run this code

```
$ python3 src/find_missing_number(lst)
```

### 3. How this program works

This program only provides a function for other scripts to use and if run as the main script simply tests its own functionality