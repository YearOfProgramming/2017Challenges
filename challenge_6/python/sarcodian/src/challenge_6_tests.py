# we start by importing the unittest module
import unittest

# Next lets import our function that we intend to do testing on
#
# **We could also import all functions by using * or just import the module
# itself but for now lets just import the function
from challenge_6 import ranges, print_range

# lets define our suite of tests as a class and lets inherit from unittest.TestCase
class TestBinaryMethods(unittest.TestCase):

    # All tests must begin with the test_* naming scheme otherwise unittest won't find it
    def test_positiveIntegers(self):
        """ Tests from the READ.me """
        # Testing input with only 1 return value
        self.assertEqual(ranges([1, 2]), ["1->2"])

# Testing input with no return value
        self.assertEqual(ranges([1]), [])

# Testing input with multiple return values
        self.assertEqual(ranges([1,2,3,4,5,8,9,10]), ["1->5", "8->10"])

# if the python file is ran by itself run unittest
# This allows us to import the members of the file without running main if we need to
if __name__ == '__main__':
    unittest.main()