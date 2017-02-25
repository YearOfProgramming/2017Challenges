#Find the Difference
###### Python 2.7.9

### 1. Approch to Solving the problem
I thought of two ways to solve this problem. The first one, pretty simple, was to iterate through string t and find which letter isn't there.
However, it would work only if we assume that there is at most one letter of each type.

This is why I decided to go for another approach that would cover the multiplicity case. I decided to use
a dictionnary to be able to keep count and know which letter is missing.
### 2. How to compile and run this code
Assuming you are within the directory under my name

To compile :
```
$ python src/FindTheDifference.py
```
To run unit tests :
```
$ python src/test.py
```
### 3. How this program works
The program doesn't allow input in itself. You can use it by import like it is done in the test.py