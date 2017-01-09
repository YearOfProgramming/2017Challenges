#!/usr/bin/env python3

import unittest
from missing_num import find_missing_num

class Tests(unittest.TestCase):

    def test1(self):
        self.assertEquals(find_missing_num([0,1,3]), 2)

    def test2(self):
        self.assertEqual(find_missing_num([0,2,3,4,1,8,7,6,5,9,11,10,12,13,15]), 14)

    def test3(self):
        self.assertEqual(find_missing_num([1,2,3]), 0)


if __name__ == '__main__':
    unittest.main()