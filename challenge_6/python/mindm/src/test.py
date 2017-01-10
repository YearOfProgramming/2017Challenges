#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import random
from ranges import find_ranges


class TestDiff(unittest.TestCase):

    def test_one_range(self):
        self.assertEqual(find_ranges([1,2,3,4,5,6,7]), ["1->7"])

    def test_two_ranges(self):
        self.assertEqual(find_ranges([1,2,3,4,5,8,9,10]), ["1->5", "8->10"])

    def test_no_range(self):
        self.assertEqual(find_ranges([1]), [])

    def test_two_ranges_one_small(self):
        self.assertEqual(find_ranges([1,2,3,4,5,8,9]), ["1->5", "8->9"])

    def test_empty_list(self):
        self.assertEqual(find_ranges([]), [])

    def test_five_lists_of_two(self):
        self.assertEqual(find_ranges([2,3,5,6,8,9,11,12,14,15]), ["2->3", "5->6", "8->9", "11->12", "14->15"])

    # def test_2(self):
        # with self.assertRaises(AssertionError):
            # find_difference("abcde", "abced")


if __name__ == '__main__':
    unittest.main()
