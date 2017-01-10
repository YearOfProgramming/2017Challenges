#!/home/shaowen/anaconda2/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:59:31 2017

@author: Shaowen Liu
"""

import unittest
import square_sort as ss

class sqaure_sort_test(unittest.TestCase):
    
    def test_case1(self):
        # for empty arr
        arr = []
        res = []
        self.assertEqual(ss.square_sort(arr),res)
    
    def test_case2(self):
        # for normal arr
        arr = [-8,-5,-2,0,6,70]
        res = [0,4,25,36,64,4900]
        self.assertEqual(ss.square_sort(arr),res)

#---- Following test is copied from slandau3's test file(deep copy, :) )
    def test1(self):
        """
        Test to make sure the program can handle a simple, ordinary input with negatives, 0 and positives
        :return:
        """
        self.assertEqual(ss.square_sort([-2,-1,0,1,2]), [0,1,1,4,4])

    def test2(self):
        """
        Test to make sure hte program can handle only negatives
        :return:
        """
        self.assertEqual(ss.square_sort([-3,-2,-1]), [1,4,9])

    def test3(self):
        """
        Test to make sure the program can handle only positives
        :return:
        """
        self.assertEqual(ss.square_sort([0,1,2,3]), [0,1,4,9])

    def test4(self):
        """
        Test to make sure the program can handle an input that does not contain zero
        :return:
        """
        self.assertEqual(ss.square_sort([-2,-1,1,2]), [1,1,4,4])

    def test5(self):
        """
        Test to make sure the program can handle a list with a bunch of different lengths between each value
        :return:
        """
        self.assertEqual(ss.square_sort([-100,-50,-2,-1,80,900,9001]), [1, 4, 2500, 6400, 10000, 810000, 81018001])

    

if __name__ == '__main__':
    unittest.main()