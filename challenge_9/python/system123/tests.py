import unittest
from challenge_9 import squared_sort

class Tests(unittest.TestCase):
	def test_pos_only(self):
		self.assertEqual( squared_sort( [1,2,4,5]), [1,4,16,25] )

	def test_neg_only(self):
		self.assertEqual( squared_sort( [-5,-4,-2,-1]), [1,4,16,25] )

	def test_mixed(self):
		self.assertEqual( squared_sort( [-5,-4,-2,-1,1,2,4,5]), [1,1,4,4,16,16,25,25] )

	def test_mixed_with_0(self):
		self.assertEqual( squared_sort( [-5,-4,-2,0,1,2,4,5]), [0,1,4,4,16,16,25,25] )


if __name__ == "__main__":
    unittest.main()