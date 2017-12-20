import unittest
from solution import findMissing

class TestRanges(unittest.TestCase):

    def test1(self):
        # Testing input with integer missing other than zero
        assert findMissing([0,1,2,4]) == 3

    def test2(self):
        # Testing input with zero missing
        assert findMissing([1,2,3]) == 0

if __name__ == '__main__':
    unittest.main()