import unittest, timeit
from challenge_13 import is_palindrome

class Tests(unittest.TestCase):
    reps = 100000

    def test_given_1(self):
        self.assertEqual(
                is_palindrome(1112111),
                True
                )
        time = timeit.timeit(
                'is_palindrome(1112111)',
                setup='from __main__ import is_palindrome',
                number=Tests.reps
                )
        print('test_given_1 completed {} reps with {}s'.format(Tests.reps, time))


    def test_given_2(self):
        self.assertEqual(
                is_palindrome(1),
                True
                )
        time = timeit.timeit(
                'is_palindrome(1)',
                setup='from __main__ import is_palindrome',
                number=Tests.reps
                )
        print('test_given_2 completed {} reps with {}s'.format(Tests.reps, time))

    def test_given_3(self):
        self.assertEqual(
                is_palindrome(59112),
                False
                )
        time = timeit.timeit(
                'is_palindrome(59112)',
                setup='from __main__ import is_palindrome',
                number=Tests.reps
                )
        print('test_given_3 completed {} reps with {}s'.format(Tests.reps, time))

    def test_given_4(self):
        self.assertEqual(
                is_palindrome(1234554321),
                True
                )
        time = timeit.timeit(
                'is_palindrome(1234554321)',
                setup='from __main__ import is_palindrome',
                number=Tests.reps
                )
        print('test_given_4 completed {} reps with {}s'.format(Tests.reps, time))

    def test_given_5(self):
        self.assertEqual(
                is_palindrome(22),
                True
                )
        time = timeit.timeit(
                'is_palindrome(22)',
                setup='from __main__ import is_palindrome',
                number=Tests.reps
                )
        print('test_given_5 completed {} reps with {}s'.format(Tests.reps, time))

    def test_given_6(self):
        self.assertEqual(
                is_palindrome(1010100101),
                False
                )
        time = timeit.timeit(
                'is_palindrome(1010100101)',
                setup='from __main__ import is_palindrome',
                number=Tests.reps
                )
        print('test_given_6 completed {} reps with {}s'.format(Tests.reps, time))

    def test_given_7(self):
        self.assertEqual(
                is_palindrome(1010110101),
                True
                )
        time = timeit.timeit(
                'is_palindrome(1010110101)',
                setup='from __main__ import is_palindrome',
                number=Tests.reps
                )
        print('test_given_7 completed {} reps with {}s'.format(Tests.reps, time))

    def test_10111(self):
        self.assertEqual(
                is_palindrome(10111),
                False
                )
        time = timeit.timeit(
                'is_palindrome(10111)',
                setup='from __main__ import is_palindrome',
                number=Tests.reps
                )
        print('test_given_10111 completed {} reps with {}s'.format(Tests.reps, time))

    def test_5014(self):
        self.assertEqual(
                is_palindrome(5014),
                False
                )
        time = timeit.timeit(
                'is_palindrome(5014)',
                setup='from __main__ import is_palindrome',
                number=Tests.reps
                )
        print('test_given_5014 completed {} reps with {}s'.format(Tests.reps, time))

if __name__ == '__main__':
    unittest.main()
