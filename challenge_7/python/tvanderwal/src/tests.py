import unittest
import random
from findMissingNumber import findMissingNumber

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEquals(findMissingNumber([0,1,3]), 2)

    def test2(self):
        self.assertEqual(findMissingNumber([0,2,3,4,1,8,7,6,5,9,11,10,12,13,15]), 14)

    def test3(self):
        self.assertEqual(findMissingNumber([1,2,3]), 0)

    def test4(self):
        a = list(range(10000001))   # Generate a super long list
        element = random.choice(a)  # Select a random element
        a.remove(element)           # Remove the random element
        self.assertEqual(findMissingNumber(a), element)

if __name__ == '__main__':
    unittest.main()