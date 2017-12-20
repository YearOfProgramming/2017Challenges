import unittest
from solution import ranges

class TestRanges(unittest.TestCase):

    def test1(self):
        # Testing input with only 1 return value
        assert ranges([1, 2]) == ["1->2"]

    def test2(self):
        # Testing input with no return value
        assert ranges([1]) == []

    def test3(self):
        # Testing input with multiple return values
        assert ranges([1,2,3,4,5,8,9,10]) == ["1->5", "8->10"]

if __name__ == '__main__':
    unittest.main()