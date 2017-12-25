import unittest
from challenge_7 import find_missing_number

class Tests(unittest.TestCase):

	def test1(self):
		self.assertEqual( find_missing_number([0,4,1,2]), 3 )

	def test2(self):
		self.assertEqual( find_missing_number([4,1,2,3]), 0 )

	def test3(self):
		self.assertEqual( find_missing_number([10,4,2,9,3,7,1,8,6,12,0,5]), 11 )


if __name__ == '__main__':
    unittest.main()