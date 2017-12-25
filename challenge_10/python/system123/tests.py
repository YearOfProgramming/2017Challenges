import unittest
from challenge_10 import check_closers

class Tests(unittest.TestCase):
	def test1(self):
		self.assertEqual(check_closers("{{{{{{{{{adfkjaefia}}}}}}}"), False)

	def test2(self):
		self.assertEqual(check_closers("{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}"), True)

	def test3(self):
		self.assertEqual(check_closers("{{{[}}}}dafda"), False)

	def test4(self):
		self.assertEqual(check_closers("{{{{{{{{{}}}}}}}}}"), True)

	def test5(self):
		self.assertEqual(check_closers("[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain"), True)

	def test6(self):
		self.assertEqual(check_closers("< blank >"), True)

	def test7(self):
		self.assertEqual(check_closers("((((((fjdalfeja((((alefjalisj(())))))))))))d"), True)

	def test8(self):
		self.assertEqual(check_closers(")))(((d"), False)

	def test9(self):
		self.assertEqual(check_closers("({)}"), False)


if __name__ == '__main__':
	unittest.main()