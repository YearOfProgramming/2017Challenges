#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import random
from missing import find_missing


class TestDiff(unittest.TestCase):

    def test_ordered(self):
        self.assertEqual(find_missing([0,1,2,3,4,5,7]), 6)

    def test_100_range(self):
        big_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
            33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
            49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65,
            66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
            82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
            98, 99]
        random.shuffle(big_range)
        self.assertEqual(find_missing(big_range), 64)

    def test_empty(self):
        self.assertEqual(find_missing([]), 0)

    def test_minimal(self):
        self.assertEqual(find_missing([0]), 1)
        
    def test_small_unordered(self):
        self.assertEqual(find_missing([3,0,1]), 2)

    def test_huge_range_shuffled(self):
        huge_range = list(range(1000))
        random.shuffle(list(huge_range))
        missing = huge_range.pop(random.randint(0,999))
        self.assertEqual(find_missing(huge_range), missing)


if __name__ == '__main__':
    unittest.main()
