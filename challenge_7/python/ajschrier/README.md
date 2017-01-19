# Challenge 7 - Find the Missing Number

*Python Version:* 2.7

In a list 0..N, find which digit is missing.

# Functions

## builtInMethod

**Input:** List
**Output:** Integer

Finds the integer 0 < x < N not present in list. The 'not in' syntax performs at O(N) according to [the Python Wiki](https://wiki.python.org/moin/TimeComplexity), so that is used to check the list for the value in the range. 

**UPDATE**: 'not in' syntax is O(N), but the fact that it's in another loop makes the solution O(N^2). Thanks erocs.

## sumMethod

**Input:** List
**Output:** Integer

Uses the principle of sequential ranges (n*n+1)/2 to find the missing element. The sum of the input list is subtracted from the sum of the full range, exposing the missing element.