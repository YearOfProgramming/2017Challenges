# we start by importing the unittest module
import unittest
from unittest import mock

# Next lets import our function that we intend to do testing on
#
# **We could also import all functions by using * or just import the module
# itself but for now lets just import the function
from challenge_12 import compress, decompress

# lets define our suite of tests as a class and lets inherit from unittest.TestCase
class TestBinaryMethods(unittest.TestCase):

    def test_compress(self):
                
        test_list = [
            'aaaaabbbbbcccccdd',
            'abcdefghhhhhijk',
            'iasudhaiusdh',
            'abcccccccccccccccde'
        ]
        
        with mock.patch('builtins.input', side_effect=test_list):
            self.assertEqual(compress(), 'a#5b#5c#5dd')
            self.assertEqual(compress(), 'abcdefgh#5ijk')
            self.assertEqual(compress(), 'iasudhaiusdh')
            self.assertEqual(compress(), 'abc#15de')
    
    def test_decompress(self):
        
        test_list = [
            'a#5b#5c#5dd',
            'abcdefgh#5ijk',
            'iasudhaiusdh'
        ]
        
        with mock.patch('builtins.input', side_effect=test_list):
            self.assertEqual(decompress(), 'aaaaabbbbbcccccdd')
            self.assertEqual(decompress(), 'abcdefghhhhhijk')
            self.assertEqual(decompress(), 'iasudhaiusdh')

    def test_decompress_with_n_digit_numbers(self):
        
        test_list = [
            'abc#15de',
            'abc#150de'
        ]
        
        with mock.patch('builtins.input', side_effect=test_list):
            self.assertEqual(decompress(), 'abcccccccccccccccde')
            self.assertEqual(decompress(), 'ab'+('c'*150)+'de')
            

# if the python file is ran by itself run unittest
# This allows us to import the members of the file without running main if we need to
if __name__ == '__main__':
    unittest.main()