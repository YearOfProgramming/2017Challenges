import unittest
from RandomPointerLinkedList import RandomPointerLinkedList

class UnitTest(unittest.TestCase):

    def testRootsToList(self):
        lists = [RandomPointerLinkedList(i, None, None) for i in range(100)]
        for i in range(len(lists)):
            if i == len(lists) - 1:
                lists[i].next = None
            else:
                lists[i].next = lists[i+1]
            lists[i].random = lists[i-1]
        roots = lists[0].rootsToList()
        for i in range(len(lists)):
            assertEqual(i, roots[i], msg=str(i) + " is not the correct value")

    def testRandomToList(self):
        lists = [RandomPointerLinkedList(i, None, None) for i in range(100)]
        for i in range(len(lists)):
            if i == len(lists) - 1:
                lists[i].next = None
            else:
                lists[i].next = lists[i+1]
            lists[i].random = lists[i-1]
        randoms = lists[0].randomToList()
        for i in range(len(lists)):
            correctVal = i if i > 0 else lists[len(lists) - 1].root
            assertEqual(correctVal, randoms[i], msg=str(i) + " is not the correct value")

    def testMakeDeepCopy(self):
        length = 100
        lists = [RandomPointerLinkedList(i, None, None) for i in range(length)]
        for i in range(len(lists)):
            if i == len(lists) - 1:
                lists[i].next = None
            else:
                lists[i].next = lists[i+1]
            lists[i].random = lists[(i + 5) % length]
        randoms = lists.randomToList()
        deepCopy = lists[0].makeDeepCopy()
        for l, r in zip(deepCopy, randoms):
            assertEqual(l.root, str(i) + "\'", msg="root value in deep copy incorrect")
            assertEqual(l.random, lists[r].root + "\'", msg = "random value in deep copy incorrect")


if __name__ == '__main__':
    unittest.main()
