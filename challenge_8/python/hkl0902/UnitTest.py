import unittest
from RandomPointerLinkedList import RandomPointerLinkedList

class UnitTest(unittest.TestCase):

    def testIterator(self):
        lists = [RandomPointerLinkedList(i, None, None) for i in range(10)]
        for i in range(len(lists)):
            if i == len(lists) - 1:
                lists[i].next = None
            else:
                lists[i].next = lists[i+1]

        head = lists[0]

    def testRootsToList(self):
        lists = [RandomPointerLinkedList(i, None, None) for i in range(10)]
        for i in range(len(lists)):
            if i == len(lists) - 1:
                lists[i].next = None
            else:
                lists[i].next = lists[i+1]
            lists[i].random = lists[i-1]
        roots = lists[0].toList()
        for i in range(len(lists)):
            self.assertEqual(i, roots[i], msg=str(i) + " is not the correct value")



if __name__ == '__main__':
    unittest.main()
