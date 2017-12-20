#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import random
from difference import find_difference

chars = list("abcdefghijklmnopqrstuvwxyz")

class TestDiff(unittest.TestCase):

    def test_1(self):
        self.assertEqual(find_difference("abcd", "abced"), "e")

    def test_2(self):
        with self.assertRaises(AssertionError):
            find_difference("abcde", "abced")

    def test_3(self):
        self.assertEqual(find_difference("abcd", "dcabe"), "e")

    def test_4(self):
        self.assertEqual(find_difference("abcdefghijklmno", "abcdefghijklmnop"), "p")

    def test_5(self):
        s1 = ''
        for i in range(100):
            s1 += random.choice(chars)
        s2 = ''.join(random.sample(s1, len(s1)))
        s2 += 'p'
        self.assertEqual(find_difference(s1, s2), "p")
        
    def test_6(self):
        s1 = ''
        for i in range(1000):
            s1 += random.choice(chars)
        s2 = ''.join(random.sample(s1, len(s1)))
        ls2 = list(s2)
        ls2.insert(random.randint(0, len(s2)), "q")
        s2 = "".join(ls2)
        self.assertEqual(find_difference(s1, s2), "q")

if __name__ == '__main__':
    unittest.main()
