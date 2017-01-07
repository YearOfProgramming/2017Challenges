Ranges
=======
Idea
------
Given a sorted list of integers, your job is to go through the list and ...

For example the input [1,2,3,4,8,9,10,12,13,14]

would return

[1->4, 8->10, 12->14]

Another example, the input [1,2,3,4,9,10,15]

would return

[1->4,9->10]

More info:
* Assume the input will not be empty
* The list will always be ordered.
* The list will only contain integers.


=======
Premise
------
Given a sorted list of integers, your job is examine the list and produce an
array of strings that represent the ranges in the format of "start->end"

Input Format
------------
* Assume the input will be a non empty
* The list will always be ordered.
* The list will only contain integers.

Example 1
---------
Given the input `[1,2,3,4,8,9,10,12,13,14]`, your function should
return:

    ["1->4", "8->10", "12->14"]

Example 2
----------
Given the input `[1,2,3,4,9,10,15]`, your function should return:

    ["1->4","9->10"]

Tests
------

If you are looking to write some tests here are some example assertions you
could implement:

```ruby
# Testing input with only 1 return value
assert ranges([1, 2]) == ["1->2"]

# Testing input with no return value
assert ranges([1]) == []

# Testing input with multiple return values
assert ranges([1,2,3,4,5,8,9,10]) == ["1->5", "8->10"]
```

Development
------------
Challenge and solution created by slandau3
