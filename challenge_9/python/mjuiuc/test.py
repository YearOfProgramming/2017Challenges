import unittest
import time
from solution import solution

def ListGenorator(start,end):
	resList = list()
	while start != end + 1:
		resList.append(start)
		start += 1
	return resList

class Test(unittest.TestCase):
	def test1(self):
		t1 = time.time()
		res = solution([])
		t2 = time.time()
		print 'Runtime test1: ' + str(t2 - t2)
		self.assertEquals(res,[])

	def test2(self):
		tlist = ListGenorator(1,20)
		t1 = time.time()
		res = solution(tlist)
		t2 = time.time()
		print 'Runtime test2: ' + str(t2 - t2)
		self.assertEquals(res,[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400])

	def test3(self):
		tlist = ListGenorator(-20,-1)
		t1 = time.time()
		res = solution(tlist)
		t2 = time.time()
		print 'Runtime test3: ' + str(t2 - t1)
		self.assertEquals(res,[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400])

	def test4(self):
		t1 = time.time()
		res = solution([-20,-19,-4,-2,0,1,2,3,4,5,6])
		t2 = time.time()
		print 'Runtime test4: ' + str(t2 - t1)
		self.assertEquals(res,[0, 1, 4, 4, 9, 16, 16, 25, 36, 361, 400])

if __name__ == '__main__':
	unittest.main()
