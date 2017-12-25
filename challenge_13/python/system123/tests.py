import unittest
from challenge_13 import is_palindrome

class Tests(unittest.TestCase):
	def test1(self):
		self.assertEqual( is_palindrome(1), True )

	def test2(self):
		self.assertEqual( is_palindrome(123456654321), True )

	def test3(self):
		self.assertEqual( is_palindrome(10302020301), True )

	def test4(self):
		self.assertEqual( is_palindrome(43243), False )

	def test5(self):
		self.assertEqual( is_palindrome(1001001011001), False )


if __name__ == "__main__":
	unittest.main()