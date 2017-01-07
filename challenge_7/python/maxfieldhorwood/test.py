import unittest

import solution

class RangeTestMethods(unittest.TestCase):

    def test_single(self):
        self.assertEqual(solution.ranges([1,2]), ['1->2'])

    def test_a_value(self):
        self.assertEqual(solution.ranges([1]), [])

    def test_multi(self):
        self.assertEqual(solution.ranges([1,2,3,5,6,7]), ['1->3','5->7'])

if __name__ == '__main__':
    unittest.main()
