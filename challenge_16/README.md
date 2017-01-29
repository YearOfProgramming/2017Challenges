Permutations
=========
Idea
-----
Your job today is to create a function that is able to determine how many possible permutations there are. For example 'abc' has 6 possible permutations --- length('abc')!

Note that your function will most likely have an absurdly high time complexity so don't test it with strings that more than 9 characters long.

The program should take a string from standard input then output the number of possible combinations (You should also implement a function to ensure that they are all unique).

Testing
-------
Here are a few test cases
abc -> ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'], 6

Since anything more than that would take up half the page, I'm just going to say the number of permutations you should output.

abcde -> 120

abcdefg -> 5040

abcdefghi -> 362880
