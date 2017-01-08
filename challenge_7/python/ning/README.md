# Challenge 7, Find The Missing Number

1. Our solution for challenge 7 comes in the form of a function `find_missing`, taking a paramter of list `input_list`.
2. We first create a set `input_set` from `input_list`. This is as it is faster to check if an element is in a set than in a list, in python.
3. We find the minimum and maximum of `input_list`, i.e. the range of the 'list of numbers from 0 to N-1'.
4. We iterate through this range from smallest to largest, checking for each integer if it exists in `input_set` (and therefore `input_list`). If it does not exist (i.e. is _missing_ from the `input_set`), return the integer.

## Learning Points

None so far. Which is suspicious, given that this is apparently a popular interview question.
