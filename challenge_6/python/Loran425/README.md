# Challenge #6 - Ranges
###### Python 3.5.2

### 0. Problem Statement

##### Premise
  * Given a sorted list of integers, your job is examine the list and produce an
    array of strings that represent the ranges in the format of "start->end"
    
##### Input Format

  * Assume the input will be a non empty
  * The list will always be ordered.
  * The list will only contain integers.  

 
---

### 1. Approach to Solving the problem

This solution looks at the given values saving the start of a range then looping over the following elements of the 
input set until it finds an element that is not equal to the previous element plus one.
Once this condition is met it is ensured that the start and end of the potential range are not the same. 
Assuming this is also true the range is appended to the output in the format specified above.
The range start is set to the number that caused the range to be evaluated and the cycle repeats 
until all the data has been processed.
 
 
---

### 2. How to run this code

```
$ python3 src/ranges.py
```

### 3. How this program works

This program only provides a function for other scripts to use and if run as the main script simply tests its own functionality