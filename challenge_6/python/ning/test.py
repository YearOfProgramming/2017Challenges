'''unittest for challenge 6 by ning
Feel free to make a copy under your
directory and use as you like.'''

import unittest
from  challenge_6 import ranges

class Tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
                ranges([]),
                []
                )

    def test_small(self):
        self.assertEqual(
                ranges([1, 2]),
                ['1->2']
                )

    def test_single(self):
        self.assertEqual(
                ranges([1]),
                []
                )

    def test_large(self):
        self.assertEqual(
                ranges([1, 2, 3, 4, 5, 8, 9, 10]),
                ['1->5', '8->10']
                )
        
    def test_larger(self):
        self.assertEqual(
                ranges([0, 1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 20, 21, 22, 23, 24, 25, 33, 44, 55, 60, 61, 62]),
                ['0->5', '7->9', '11->13', '20->25', '60->62']
                )

    def test_largest(self):
        self.assertEqual(
                ranges([1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 20, 25, 26, 27, 28, 29, 30, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44,77, 78, 79, 80, 100, 101, 102, 103, 104, 105, 106, 107, 108, 200, 1001, 1002, 1003, 1234, 1235, 1236, 1237, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2080]),
                ['1->5', '10->15', '25->30', '33->37', '40->44', '77->80', '100->108', '1001->1003', '1234->1237', '1996->2017']
                )

    def test_negatives(self):
        self.assertEqual(
                ranges([-20, -19, -18, -17, -16, -3, -2, -1, 0, 1, 2, 3, 10, 11, 12, 13, 14]),
                ['-20->-16', '-3->3', '10->14']
                )


if __name__ == '__main__':
    unittest.main()

