from IntRange import outputRange
import unittest


class outputRangeTests(unittest.TestCase):
    """test outputRange Function"""
    def test1(self):
        self.assertEqual(outputRange([1, 2, 3, 4, 8, 9, 10, 12, 13, 14]),
                         ["1->4", "8->10", "12->14"])

    def test2(self):
        self.assertEqual(outputRange([1, 2, 3, 4, 5, 8, 9, 10]),
                         ["1->5", "8->10"])

    def test3(self):
        self.assertEqual(outputRange([]),
                         [])

if __name__ == '__main__':
    unittest.main()
