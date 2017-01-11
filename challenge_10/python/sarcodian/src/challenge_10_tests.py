# we start by importing the unittest module
import unittest

# Next lets import our function that we intend to do testing on
#
# **We could also import all functions by using * or just import the module
# itself but for now lets just import the function
from challenge_10 import brackets

# lets define our suite of tests as a class and lets inherit from unittest.TestCase
class TestBinaryMethods(unittest.TestCase):

    def test_squareSort(self):
        """ Tests from the READ.me used to test the non input version"""
        
        self.assertEqual(brackets('{{{{{{{{{adfkjaefia}}}}}}}'), False)
        self.assertEqual(brackets('{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}'), True)
        self.assertEqual(brackets('{{{[}}}}dafda'), False)
        self.assertEqual(brackets('{{{{{{{{{}}}}}}}}}'), True)
        self.assertEqual(brackets('[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain'), True)
        self.assertEqual(brackets('< blank >'), True)
        self.assertEqual(brackets('((((((fjdalfeja((((alefjalisj(())))))))))))d'), True)
        self.assertEqual(brackets(')))(((d'), False)
        self.assertEqual(brackets('({)} '), False)

        

# if the python file is ran by itself run unittest
# This allows us to import the members of the file without running main if we need to
if __name__ == '__main__':
    unittest.main()