# Find the Difference

### 1. Approch to Solving the problem

My approach to solving this problem is to first find the largest character
in the given set of characters by ASCII value for the pair of strings

Once I have the largest characters, I create a counting array that counts
the numbers the characters in each strings. the length of the count arrays
is the length of the ASCII value of the largest character in each string
with all the values set to 0.

I then iterate through the strings and increment the value of
each index of the count array for each ASCII value of the pair
of strings.

Example:
s = abc
t = abce

I create a count array of size 'c' with all 0s.
I create a count array of size 'e' with all 0s.

As I iterate through those strings I increment the matching index value
for the corresponding ASCII value of that string.

The index that contains a differing count value is the different character.

If all the values end up being equal up until the size of the shorter string,
then the max ASCII value of the larger string is the different character.

### 2. How to compile and run this code

Assuming you are within the directory under my name

```
$ make
```

### 3. How this program works

This program takes in 2 lines of standard input and prints out the different integer

It does not handle mixed characters

