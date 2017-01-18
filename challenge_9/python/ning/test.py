import unittest, timeit
from challenge_9 import square_sort

class Tests(unittest.TestCase):
    reps = 100000

    def test_positives(self):
        self.assertEqual(
                square_sort([1, 2, 3, 4]),
                [1, 4, 9, 16]
                )
        time = timeit.timeit(
                'square_sort([1, 2, 3, 4])',
                setup='from __main__ import square_sort',
                number=Tests.reps
                )
        print('test_positives completed {} reps with {}s'.format(Tests.reps, time))


    def test_negatives(self):
        self.assertEqual(
                square_sort([-1, -2, -3, -4]),
                [1, 4, 9, 16]
                )
        time = timeit.timeit(
                'square_sort([-1, -2, -3, -4])',
                setup='from __main__ import square_sort',
                number=Tests.reps
                )
        print('test_negatives completed {} reps with {}s'.format(Tests.reps, time))

    def test_zeroes_positives(self):
        self.assertEqual(
                square_sort([0, 0, 1, 3, 5]),
                [0, 0, 1, 9, 25]
                )
        time = timeit.timeit(
                'square_sort([0, 0, 1, 3, 5])',
                setup='from __main__ import square_sort',
                number=Tests.reps
                )
        print('test_zeroes_positives completed {} reps with {}s'.format(Tests.reps, time))

    def test_zeroes_negatives(self):
        self.assertEqual(
                square_sort([-6, -4, -2, 0, 0]),
                [0, 0, 4, 16, 36]
                )
        time = timeit.timeit(
                'square_sort([-6, -4, -2, 0, 0])',
                setup='from __main__ import square_sort',
                number=Tests.reps
                )
        print('test_zeroes_negatives completed {} reps with {}s'.format(Tests.reps, time))

    def test_all(self):
        self.assertEqual(
                square_sort([-10, -8, -5, -3, -1, 0, 2, 4, 6, 7, 9]),
                [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
                )
        time = timeit.timeit(
                'square_sort([-10, -8, -5, -3, -1, 0, 2, 4, 6, 7, 9])',
                setup='from __main__ import square_sort',
                number=Tests.reps
                )
        print('test_all completed {} reps with {}s'.format(Tests.reps, time))

    def test_repeats(self):
        self.assertEqual(
                square_sort([-10, -8, -5, -3, -2, -1, 0, 0, 2, 4, 5, 6, 7, 9, 10]),
                [0, 0, 1, 4, 4, 9, 16, 25, 25, 36, 49, 64, 81, 100, 100]
                )
        time = timeit.timeit(
                'square_sort([-10, -8, -5, -3, -2, -1, 0, 0, 2, 4, 5, 6, 7, 9, 10])',
                setup='from __main__ import square_sort',
                number=Tests.reps
                )
        print('test_repeats completed {} reps with {}s'.format(Tests.reps, time))

if __name__ == '__main__':
    unittest.main()


