import unittest
from MissingNumber import MissingNumber

class UnitTest(unittest.TestCase):

    def testMissingNumber(self):
        for i in range(5):
            mn = MissingNumber([k for k in range(5) if k != i])
            self.assertEqual(i, mn.findMissingNum())

if __name__ == '__main__':
    unittest.main()
