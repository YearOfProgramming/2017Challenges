# Integer Palindrome

### Challenge

Another classic problem. A palindrome is a word that is the same when read forward or backward, like **racecar** or **tacocat**.
Write a program that takes in a positive integer value **(12321)**, and returns boolean **(true)** if the integer is a palindrome.

The program should take a number from standard input (this is the only time you will be allowed to perform a cast) and use that as the number to be checked. The resulting boolean should be outputted to standard output.

### Constraints
1. Your program must not use any "built-in" methods or classes, only generics.
2. This means nothing like *String.valueOf()* or *.equals()* or *.reverse()*
3. **Your program must not use Strings or Characters in any form. Only numbers (integers/doubles)**

Input can be expected to have at least 1 digit and all digits are positive.
Input will not have any leading or trailing 0s like **0123210** but **1230550321** is acceptable input.

Your program should run in O(n) time with O(n) space.

### Example

In: 1112111
Out: true

In: 1 
Out: true

In: 59112 
Out: false

In: 1234554321
Out: true

In: 22
Out: true

In: 1010100101
Out: false

In: 1010110101
Out: true

Testing
------
The test cases can be found in the tests directory. The program, when tested with the test cases should output the boolean listed.
* test1: true
* test2: true
* test3: false
* test4: false
* test5: true

Challenge created by @jdfurlan
