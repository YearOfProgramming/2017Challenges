import unittest
from main import rangefinder

class TestDiff(unittest.TestCase):

    def test_one_range(self):
        self.assertEqual(rangefinder([1,2,3,4,5,6,7]), ["1->7"])

    def test_two_ranges(self):
        self.assertEqual(rangefinder([1,2,3,4,5,8,9,10]), ["1->5", "8->10"])

    def test_no_range(self):
        self.assertEqual(rangefinder([1]), [])

    def test_two_ranges_one_small(self):
        self.assertEqual(rangefinder([1,2,3,4,5,8,9]), ["1->5", "8->9"])

    def test_empty_list(self):
        self.assertEqual(rangefinder([]), [])

    def test_five_lists_of_two(self):
        self.assertEqual(rangefinder([2,3,5,6,8,9,11,12,14,15]), ["2->3", "5->6", "8->9", "11->12", "14->15"])
        
if __name__ == '__main__':
    unittest.main()