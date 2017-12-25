import unittest
from challenge_12 import compress, decompress

class Tests(unittest.TestCase):
    def test_compress_none(self):
        self.assertEqual(
                compress('abcdefghijklmnopqrstuvwxyz'),
                'abcdefghijklmnopqrstuvwxyz'
                )

    def test_compress_little(self):
        self.assertEqual(
                compress('aaaaabbbbbccccc'),
                'a#5b#5c#5'
                )

    def test_compress_few(self):
        self.assertEqual(
                compress('aaaaaaabbbkjhoooooooo'),
                'a#7bbbkjho#8'
                )

    def test_decompress_none(self):
        self.assertEqual(
                decompress('abcdefghijklmnopqrstuv'),
                'abcdefghijklmnopqrstuv'
                )

    def test_decompress_little(self):
        self.assertEqual(
                decompress('a#5b#5c#5'),
                'aaaaabbbbbccccc'
                )

    def test_decompress_few(self):
        self.assertEqual(
                decompress('a#7bbbkjho#8'),
                'aaaaaaabbbkjhoooooooo'
                )

if __name__ == '__main__':
    unittest.main()
    
