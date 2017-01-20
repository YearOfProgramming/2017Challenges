import unittest
from challenge_13 import check_palindrome

class Tests(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(
                check_palindrome(1112111),
                True
                )

    def test_given_2(self):
        self.assertEqual(
                check_palindrome(1),
                True
                )

    def test_given_3(self):
        self.assertEqual(
                check_palindrome(59112),
                False
                )

    def test_given_4(self):
        self.assertEqual(
                check_palindrome(1234554321),
                True
                )

    def test_given_5(self):
        self.assertEqual(
                check_palindrome(22),
                True
                )

    def test_given_6(self):
        self.assertEqual(
                check_palindrome(1010100101),
                False
                )

    def test_given_7(self):
        self.assertEqual(
                check_palindrome(1010110101),
                True
                )

    def test_10111(self):
        self.assertEqual(
                check_palindrome(10111),
                False
                )

if __name__ == '__main__':
    unittest.main()
