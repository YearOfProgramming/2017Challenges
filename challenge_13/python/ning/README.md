# Challenge #13, Integer Palindrome

## Solution Logic

1. We run through conditionals to check for non-palindromic integers. If they pass these tests, we assume them to be palindromic.
2. Single-digit integers are by definition (of this challenge, anyway) palindromes. These skip the main `while` loop and the function returns True straight away. For the rest...
3. First, we store the last digit (in the ones position) in the variable `ones`. In this process, the last digit of the given integer is also made to be zero.
4. Assuming the given integer is palindromic, we subtract the first digit, hence removing it. Next, divide the integer by 10 to remove the last integer. Hence, two digits from each end of the given integer is stripped off. Following this, there are 4 cases to consider.

_Case 1_: 514 -> 11
In this non-palindromic case, we end up after step (4) with the integer 11. The first digit was not stripped as it was larger than the last digit. As such, only one digit was stripped. We test for this case where the difference in digits after step (4) is only 1, and return False.

_Case 2_: 415 -> -90
This is our second non-palindromic case. As the first digit is smaller than the last, we end up with a negative integer. Testing for this is easy: `if _int < 0`. Naturally, the function returns False in this case.

_Case 3_: 515 -> 1
The ideal scenario. We end up with 1, and a difference of two digits. Since there is only one digit, the function breaks out of the while loop and returns True.

_Case 4_: 10101 -> 10
Tricky. We remove the two digits at both ends to get `010`, but the program reads this as `10`. To rememdy this, we detect the extra difference in digits (three stripped instead of two), and divide by 10 for each starting zero, getting `1` instead of `10`.

_Case 5_: 10111-> 11
A subset of _Case 4_, we detect a three digit difference, and the program continues as in the previous case to divide an extra time by 10, giving us `1.1`. Hence we must include an `if _int % 1 != 0` to detect for this case.

## Functions

1. `get_int_len` takes an integer input and returns the number of digits in that integer by comparing it to powers of 10. A more mathematical way to do this would be with log of base 10, but this would violate rule #1 with its use of the `math` module.
2. `check_palindrome` takes an integer input and returns True if it is an integer palindrome, and False if not.
3. `check_palindrome_str `is a wrapper around the above `check_palindrome` function which takes a string input instead.


## Unit Test

The unit test `test.py` consists of the seven examples provided in the challenge README.md, as well as a test case for the above descripted _Case 5_.

```
........
----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```

