import unittest

from challenge2 import findSingleton

class TestFindSingleton(unittest.TestCase):
    def test_base_case(self):
        aList = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7]
        bList = [2,'a', 'l', 3, 'l', 4, 'k', 2, 3, 4, 5, 'a', 6, 'c', 4, 'm', 6, 'm', 'k', 9, 10, 9, 8, 7, 8, 10, 7]

        self.assertEqual(findSingleton(aList), [5])
        self.assertEqual(findSingleton(bList), ['c', 5])

    def test_empty(self):
        aList = []
        bList = [1, 1, 1]

        self.assertEqual(findSingleton(aList), [])
        self.assertEqual(findSingleton(bList), [])

    def test_similiar_ascii(self):
        aList = [73, 'I']

        self.assertEqual(findSingleton(aList), ['I', 73])

if __name__ == '__main__':
    unittest.main()
