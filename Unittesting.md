# Unit Testing in Python

This tutorial will not teach you everything you should know about Unit Testing but it should give you enough to get started.

## Why do we unit test?

Unit tests are used to design code. It is not the same as testing code. When we write unit tests we are writing the normal behavior and we should be thinking about the edge cases or what could break our code and how it should be handled. We want to write robust and reusable code.

Take for example the following function:

File: binary_methods.py
```Python
# Python3 Syntax for log2
import math

def size_of_binary(n):
    """ Returns the number of binary positions needed to represent an integer n """
    return math.floor(math.log2(n) + 1)

print(size_of_binary(1))
>>> 1
print(size_of_binary(3))
>>> 2
print(size_of_binary(5))
>>> 3
```
Awesome so it works, right?
Well..
```Python
print(size_of_binary(0))

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: math domain error
```
Crap, well what happened?

Turns out we can't take the log of zero, this is one of those edge cases I was talking about. If we wrote some unit tests we may have caught this early on. Unit tests should be written before we write code. In this way we can begin to design our code and it should conform to our tests. When our code passes our unit tests we can gain confidence about the validity of our code. It also allows us to make changes to our existing code and know instantly if it broke preexisting behavior.

Lets rewind a bit and think about Unit Tests.

## Unit Testing
In python unit testing is very easy. In fact python comes with a Unit testing framework built in, the unittest module.

To begin lets create a new file in the same directory as our python code will be in (Usually tests should be broken off into a test/ folder but for simplicity lets not.)

File: binary_tests.py
```Python
# we start by importing the unittest module
import unittest

# Next lets import our function that we intend to do testing on
#
# **We could also import all functions by using * or just import the module
# itself but for now lets just import the function
from binary_methods import size_of_binary

# lets define our suite of tests as a class and lets inherit from unittest.TestCase
class TestBinaryMethods(unittest.TestCase):

    # All tests must begin with the test_* naming scheme otherwise unittest won't find it
    def test_positiveIntegers(self):
        """ We expect the size of a positive integer to be the number of bits in binary """
        self.assertEqual(size_of_binary(1), 1)
        self.assertEqual(size_of_binary(4), 3)
        self.assertEqual(size_of_binary(100), 7)

    def test_zero(self):
        """ We expect size_of_binary(0) to return 1 """
        self.assertEqual(size_of_binary(0), 1)

    def test_negativeIntegers(self):
        """ We expect the size of a negative number to be the same as its absolute value """

        # Another way we could handle this is adding another bit at the front that signifies
        # the sign ie 5 = 101 so size is 3, however 0101 for +5 and size 4
        # and 1101 for -5 and size 4
        self.assertEqual(size_of_binary(-1), 1)
        self.assertEqual(size_of_binary(-4), 3)
        self.assertEqual(size_of_binary(-100), 7)

# if the python file is ran by itself run unittest
# This allows us to import the members of the file without running main if we need to
if __name__ == '__main__':
    unittest.main()

```

Now that we have our tests written lets go back to our binary_methods file. With our tests written lets think about our function.

File: binary_methods.py
```Python
# Python3 Syntax for log2
import math

def size_of_binary(n):
    """ Returns the number of binary positions needed to represent an integer n """
    # if n is zero lets just return 1 to guard log2
    if n == 0:
        return 1

    # lets use the abs() function to handle negatives
    return math.floor(math.log2(abs(n)) + 1)
```

And finally we run our unit test file.
```Bash
> $ python3 binary_tests.py                                            ⬡ 7.2.0
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

Success nothing broke! We successfully handled the conditions that we had intended to
design for.

If something did break we would have seen something like:

```Bash
> $ python3 binary_tests.py                                            ⬡ 7.2.0
..F
======================================================================
FAIL: test_zero (__main__.TestBinaryMethods)
We expect size_of_binary(0) to return 1
----------------------------------------------------------------------
Traceback (most recent call last):
  File "binary_tests.py", line 23, in test_zero
    self.assertEqual(size_of_binary(0), 0)
AssertionError: 1 != 0

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

# For more information check out:
Links:
* [UnitTest for Python2](https://docs.python.org/2/library/unittest.html)
* [UnitTest for Python3](https://docs.python.org/3/library/unittest.html)

Theres a bunch more asserts we can do such as assertTrue. I just gave the simplest case. I highly recommend skimming over the docs and learning more.