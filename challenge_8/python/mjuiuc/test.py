import unittest
import random
import time
from listNode import listNode
from solution import solution

class Tests(unittest.TestCase):
	def test1(self):
		# create linked list
		temp = listNode()
		head = temp
		lop = list()
		for i in xrange(1,11):
			lop.append(temp)
			temp.val = i
			temp.next = listNode()
			temp = temp.next
		# assign random pointers
		temp2 = head
		while temp2 != None:
			temp2.random = lop[random.randint(0,9)]
			temp2 = temp2.next
		# get the copied list head
		t1 = time.time()
		copiedHead = solution(head)
		t2 = time.time()
		# can't figure out a nice way to check the random pointers..
		for i in lop:
			# the actual test happens here
			assert copiedHead.val == head.val, "error in value"
			assert copiedHead.random.val == head.random.val, "error in random value"
			copiedHead = copiedHead.next
			head = head.next
		print 'Runtime of test1: ' + str(t2 - t1)

	def test2(self):
		# create linked list
		temp = listNode()
		head = temp
		lop = list()
		for i in xrange(1,10001):
			lop.append(temp)
			temp.val = i
			temp.next = listNode()
			temp = temp.next
		# assign random pointers
		temp2 = head
		while temp2 != None:
			temp2.random = lop[random.randint(0,9999)]
			temp2 = temp2.next
		# get the copied list head
		t1 = time.time()
		copiedHead = solution(head)
		t2 = time.time()
		# can't figure out a nice way to check the random pointers..
		for i in lop:
			# the actual test happens here
			assert copiedHead.val == head.val, "error in value"
			assert copiedHead.random.val == head.random.val, "error in random value"
			copiedHead = copiedHead.next
			head = head.next
		print 'Runtime of test2: ' + str(t2 - t1)

	def test3(self):
		# create linked list
		temp = listNode()
		head = temp
		lop = list()
		for i in xrange(1,100001):
			lop.append(temp)
			temp.val = i
			temp.next = listNode()
			temp = temp.next
		# assign random pointers
		temp2 = head
		while temp2 != None:
			temp2.random = lop[random.randint(0,99999)]
			temp2 = temp2.next
		# get the copied list head
		t1 = time.time()
		copiedHead = solution(head)
		t2 = time.time()
		# can't figure out a nice way to check the random pointers..
		for i in lop:
			# the actual test happens here
			assert copiedHead.val == head.val, "error in value"
			assert copiedHead.random.val == head.random.val, "error in random value"
			copiedHead = copiedHead.next
			head = head.next
		print 'Runtime of test3: ' + str(t2 - t1)

if __name__ == '__main__':
	unittest.main()
