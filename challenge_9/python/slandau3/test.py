#!/usr/bin/env python3
# @author slandau3

import unittest
from square import reorder


class Tests(unittest.TestCase):

    def test1(self):
        """
        Test to make sure the program can handle a simple, ordinary input with negatives, 0 and positives
        :return:
        """
        self.assertEqual(reorder([-2,-1,0,1,2]), [0,1,1,4,4])

    def test2(self):
        """
        Test to make sure hte program can handle only negatives
        :return:
        """
        self.assertEqual(reorder([-3,-2,-1]), [1,4,9])

    def test3(self):
        """
        Test to make sure the program can handle only positives
        :return:
        """
        self.assertEqual(reorder([0,1,2,3]), [0,1,4,9])

    def test4(self):
        """
        Test to make sure the program can handle an input that does not contain zero
        :return:
        """
        self.assertEqual(reorder([-2,-1,1,2]), [1,1,4,4])

    def test5(self):
        """
        Test to make sure the program can handle a list with a bunch of different lengths between each value
        :return:
        """
        self.assertEqual(reorder([-100,-50,-2,-1,80,900,9001]), [1, 4, 2500, 6400, 10000, 810000, 81018001])


if __name__ == '__main__':
    unittest.main()