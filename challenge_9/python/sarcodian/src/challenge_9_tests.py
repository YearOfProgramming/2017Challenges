# we start by importing the unittest module
import unittest

# Next lets import our function that we intend to do testing on
#
# **We could also import all functions by using * or just import the module
# itself but for now lets just import the function
from challenge_9 import square_n_sort

# lets define our suite of tests as a class and lets inherit from unittest.TestCase
class TestBinaryMethods(unittest.TestCase):

    def test_squareSort(self):
        """ Tests from the READ.me """
        
        self.assertEqual(square_n_sort([0,1,2]), [0,1,4])
        self.assertEqual(square_n_sort([-5,-4,-3,-2]), [4,9,16,25])
        self.assertEqual(square_n_sort([1,2]), [1,4])
        self.assertEqual(square_n_sort([-2,-1,0,1,2]), [0,1,1,4,4])

# if the python file is ran by itself run unittest
# This allows us to import the members of the file without running main if we need to
if __name__ == '__main__':
    unittest.main()