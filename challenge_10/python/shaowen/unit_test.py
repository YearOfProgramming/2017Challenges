# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:21:20 2017

@author: Shaowen Liu
"""
import unittest
from solution import solution

class solution_test(unittest.TestCase):
    
    def test_case1(self):
        strr = '{{{}}}'
        self.assertTrue(solution(strr))
    
    def test_case2(self):
        strr = '{{{{{{{{{adfkjaefia}}}}}}}'
        self.assertFalse(solution(strr))

    def test_case3(self):
        strr = '{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}'
        self.assertTrue(solution(strr))

    def test_case4(self):
        strr = '{{{[}}}}'
        self.assertFalse(solution(strr))
        
    def test_case5(self):
        strr = '{{{{{{{{{}}}}}}}}}'
        self.assertTrue(solution(strr))

    def test_case6(self):
        strr = '[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain'
        self.assertTrue(solution(strr))

    def test_case7(self):
        strr = '([{)}]'
        self.assertFalse(solution(strr))

if __name__ == '__main__':
    unittest.main()
