# Challenge 7 - Find the Missing Number

In a list 0..N, find which digit is missing.

# Functions

## builtInMethod

**Input:** List
**Output:** Integer

 Finds the integer 0 < x < N not present in list. The 'not in' syntax performs at O(N) according to [the Python Wiki](https://wiki.python.org/moin/TimeComplexity), so that is used to check the list for the value in the range. 