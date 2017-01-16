#!/usr/bin/env python3

import unittest
from compression import compress, decompress

class Test(unittest.TestCase):

    def test1(self):
        """
        A small standard string
        :return:
        """
        self.assertEqual(compress('aaaaa'), 'a#5')

    def test2(self):
        """
        An arbitrarily long string
        :return:
        """
        self.assertEqual(compress('abadbadsakdlfjieafnealfjiasfjaaaaanadddddddkkkjj'), "abadbadsakdlfjieafnealfjiasfja#5nad#7kkkjj")

    def test3(self):
        """
        A string where a lot has to be compressed
        :return:
        """
        self.assertEqual(compress('kkkkkkjjjjjjjnnnnniiiiiiiooooook'), 'k#6j#7n#5i#7o#6k')

    def test4(self):
        """
        Decompressing a small string
        :return:
        """
        self.assertEqual(decompress('a#5'), 'aaaaa')

    def test5(self):
        """
        Decompress a fairly large string without too many compressions in it.
        :return:
        """
        self.assertEqual(decompress('abadbadsakdlfjieafnealfjiasfja#5nad#7kkkjj'), 'abadbadsakdlfjieafnealfjiasfjaaaaanadddddddkkkjj')

    def test6(self):
        """
        Decompress a string with a lot of compressions in it
        :return:
        """
        self.assertEqual(decompress('k#6j#7n#5i#7o#6k'), 'kkkkkkjjjjjjjnnnnniiiiiiiooooook')


if __name__ == '__main__':
    unittest.main()