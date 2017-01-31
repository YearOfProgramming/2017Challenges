# we start by importing the unittest module
import unittest
from unittest import mock

# Next lets import our function that we intend to do testing on
#
# **We could also import all functions by using * or just import the module
# itself but for now lets just import the function
from challenge_10 import brackets

# lets define our suite of tests as a class and lets inherit from unittest.TestCase
class TestBinaryMethods(unittest.TestCase):

    def test_Brackets(self):
        """ Tests from the READ.me """
        
        test_list = [
            '{{{{{{{{{adfkjaefia}}}}}}}',
            '{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}',
            '{{{[}}}}dafda',
            '{{{{{{{{{}}}}}}}}}',
            '[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain',
            '< blank >',
            '((((((fjdalfeja((((alefjalisj(())))))))))))d',
            ')))(((d',
            '({)} '
        ]
        
        with mock.patch('builtins.input', side_effect=test_list):
            self.assertEqual(brackets(), False)
            self.assertEqual(brackets(), True)
            self.assertEqual(brackets(), False)
            self.assertEqual(brackets(), True)
            self.assertEqual(brackets(), True)
            self.assertEqual(brackets(), True)
            self.assertEqual(brackets(), True)
            self.assertEqual(brackets(), False)
            self.assertEqual(brackets(), False)

        

# if the python file is ran by itself run unittest
# This allows us to import the members of the file without running main if we need to
if __name__ == '__main__':
    unittest.main()