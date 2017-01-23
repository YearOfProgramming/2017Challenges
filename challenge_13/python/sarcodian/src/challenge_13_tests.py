# we start by importing the unittest module
import unittest
from unittest import mock

# Next lets import our function that we intend to do testing on
#
# **We could also import all functions by using * or just import the module
# itself but for now lets just import the function
from challenge_13 import int_palin

# lets define our suite of tests as a class and lets inherit from unittest.TestCase
class TestBinaryMethods(unittest.TestCase):

    def test_int_palin(self):
                
        test_list = [
            '1112111',
            '1',
            '59112',
            '1234554321',
            '22',
            '1010100101',
            '1010110101'
        ]
        
        with mock.patch('builtins.input', side_effect=test_list):
            self.assertEqual(int_palin(), True)
            self.assertEqual(int_palin(), True)
            self.assertEqual(int_palin(), False)
            self.assertEqual(int_palin(), True)
            self.assertEqual(int_palin(), True)
            self.assertEqual(int_palin(), False)
            self.assertEqual(int_palin(), True)
            
# if the python file is ran by itself run unittest
# This allows us to import the members of the file without running main if we need to
if __name__ == '__main__':
    unittest.main()