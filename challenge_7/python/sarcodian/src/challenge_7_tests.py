# we start by importing the unittest module
import unittest

# Next lets import our function that we intend to do testing on
#
# **We could also import all functions by using * or just import the module
# itself but for now lets just import the function
from challenge_7 import missing_int

# lets define our suite of tests as a class and lets inherit from unittest.TestCase
class TestBinaryMethods(unittest.TestCase):

    def test_missingInt(self):
        
        self.assertEqual(missing_int([1,3,4,0]), 2)
        self.assertEqual(missing_int([1,2,3]), 0)
        self.assertEqual(missing_int([0,1,2,4]), 3)

# if the python file is ran by itself run unittest
# This allows us to import the members of the file without running main if we need to
if __name__ == '__main__':
    unittest.main()