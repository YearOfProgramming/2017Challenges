import unittest
from challenge_6 import ranges

class Tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual( ranges([]), [] )

    def test_single(self):
        self.assertEqual( ranges([1,2]), ['1->2'] )

    def test_two_ranges(self):
        self.assertEqual( ranges([1,2,3,4,7,8,9]), ['1->4','7->9'] )

    def test_three_ranges(self):
        self.assertEqual( ranges([1,2,3,4,8,9,10,12,13,14]), ['1->4','8->10', '12->14'] )

    def test_negatives(self):
        self.assertEqual( ranges([-20, -19, -18, -17, -16, -3, -2, -1, 0, 1, 2, 3, 10, 11, 12, 13, 14]), ['-20->-16', '-3->3', '10->14'])

if __name__ == '__main__':
    unittest.main()