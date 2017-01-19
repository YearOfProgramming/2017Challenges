import unittest
import time
from challenge_9 import square_sort


class Tests(unittest.TestCase):

	def test1(self):
		t1 = time.time()
		self.assertEqual(square_sort([-3, -2, -1, 0, 1, 2, 3]),[0, 1, 1, 4, 4, 9, 9])
		t2 = time.time()
		print('Runtime test1: ' + str(t2-t1))

	def test2(self):
		t1 = time.time()
		self.assertEqual(square_sort([4, 5, 6]),[16, 25, 36])
		t2 = time.time()
		print('Runtime test1: ' + str(t2-t1))

	def test3(self):
		t1 = time.time()
		self.assertEqual(square_sort([-11, -10, -9]),[81, 100, 121])
		t2 = time.time()
		print('Runtime test1: ' + str(t2-t1))


if __name__ == '__main__':
	unittest.main()