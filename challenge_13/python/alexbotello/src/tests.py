import unittest
from palin import is_palindrome

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_palindrome(1112111), True)

    def test_2(self):
        self.assertEqual(is_palindrome(1), True)

    def test_3(self):
        self.assertEqual(is_palindrome(59112), False)

    def test_4(self):
        self.assertEqual(is_palindrome(1234554321), True)

    def test_5(self):
        self.assertEqual(is_palindrome(22), True)

    def test_6(self):
        self.assertEqual(is_palindrome(1010100101), False)

    def test_7(self):
        self.assertEqual(is_palindrome(1010110101), True)


if __name__ == '__main__':
    unittest.main()
