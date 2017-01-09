# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 08:21:07 2017

@author: Shaowen Liu
"""

import unittest
import findMissing as fm

class findMissing_test(unittest.TestCase):
    
    def test_case1(self):
        arr = [0,1,3,4]
        res = 2
        self.assertEqual(fm.findMissing(arr),res)

    def test_case2(self):
        arr = [1,2,3]
        res = 0
        self.assertEqual(fm.findMissing(arr),res)

if __name__ == '__main__':
    unittest.main()