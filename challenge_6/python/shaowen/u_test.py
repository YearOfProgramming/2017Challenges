# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 09:21:40 2017

@author: Shaowen liu
"""

import unittest
import ranges

class ranges_test(unittest.TestCase):
    
    def test_case1(self):
        """
        Testing input with only 1 return value
        """
        arr = [1,2]
        res = ["1->2"]
        self.assertEqual(ranges.ranges(arr), res)
        
    def test_case2(self):
        """
        Testing input with no return value
        """
        arr = []
        res = []
        self.assertEqual(ranges.ranges(arr), res)
        
    def test_case3(self):
        """
        Testing input with multiple return values
        """
        arr = [1,2,3,4,5,8,9,10]
        res = ["1->5", "8->10"]
        self.assertEqual(ranges.ranges(arr), res)


if __name__ == '__main__':
    unittest.main()
        


