import unittest
from challenge_9 import square_sort

class Tests(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(
                square_sort([1, 2, 3, 4]),
                [1, 4, 9, 16]
                )

    def test_negatives(self):
        self.assertEqual(
                square_sort([-1, -2, -3, -4]),
                [1, 4, 9, 16]
                )

    def test_zeroes_positives(self):
        self.assertEqual(
                square_sort([0, 0, 1, 3, 5]),
                [0, 0, 1, 9, 25]
                )

    def test_zeroes_negatives(self):
        self.assertEqual(
                square_sort([-6, -4, -2, 0, 0]),
                [0, 0, 4, 16, 36]
                )

    def test_all(self):
        self.assertEqual(
                square_sort([-10, -8, -5, -3, -1, 0, 2, 4, 6, 7, 9]),
                [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
                )
    def test_repeats(self):
        self.assertEqual(
                square_sort([-10, -8, -5, -3, -2, -1, 0, 0, 2, 4, 5, 6, 7, 9, 10]),
                [0, 0, 1, 4, 4, 9, 16, 25, 25, 36, 49, 64, 81, 100, 100]
                )

if __name__ == '__main__':
    unittest.main()


