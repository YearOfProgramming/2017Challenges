#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import random
from compression import compress, decompress


class TestComp(unittest.TestCase):

    def test_1(self):
        self.assertEqual(decompress("a#5"), "aaaaa")

    def test_2(self):
        self.assertEqual(compress("abbcccddddeeeee"), "abbcccd#4e#5")

    def test_3(self):
        original = "aliiiiicia foooooooohx"
        compressed = compress(original)
        decompressed = decompress(compressed)
        self.assertEqual(original, decompressed)

    def test_long(self):
        self.assertEqual(compress("fooooooooooooooox"), "fo#15x")

    def test_long2(self):
        self.assertEqual(decompress("fo#15x"), "fooooooooooooooox")

if __name__ == '__main__':
    unittest.main()