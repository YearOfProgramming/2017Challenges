# Challenge #13, Integer Palindrome

This challenge was revisited on the request of @slandau.

## Solution Logic

`is_palindrome` is a recursive function that checks if an integer is a palindrome. It consists of some base cases, followed by some reduction/simplifying of the given integer input.

### Base Cases

There are three base cases being checked for,

1. `if len_pre == -1`: if the function `get_len` returns -1 for the given number. This is the case whereby the function has already run through some loops, and has reached a point where the given integer input has been simplified to a non-integer. This happens in the case of a non-palindromic integer input where there is a non-palindromic/symmetrical 0, e.g. 10111 -> 011 -> 1.1

2. `elif len_pre == 0 or len_pre == 1`: integers of length 1 or 0 are by the given definition, palindromes.

3. `elif len_pre == 2`: we return `_int % 11 == 0`, i.e. for all multiples of 11 before 100 (this covers all palindromic integers from 0 to 100 inclusive).

### Reduction/Simplification

1. Find the last digit (in the ones place) with `_int % 10`.
2. Subtract from `_int` it's last digit and divide by 10 (i.e. remove last digit)
3. Subtract from `_int` the last digit * 10\*\* (len\_pre-2) (i.e. remove first digit)
4. If the difference in lengths of the `_int` before and after is greater than two, this indicates that there was an extra 0 at the integer after the steps (2) and (3) that was ignored by the program. To account for this, we divide addtionally by 10 for each extra zero at the start. _If_ the first digit was zero but the last digit is not, this will result in a non-integer being passed on in the next recursion that is caught by base case (1).

_Note_: There is a check here for if the difference in digits is less than two. This is essential so that things like (5014 -> 101) don't get through.

## Unit Test

Unit test, `test.py` consists of the seven examples given as well as two extras (10111 & 5014).
