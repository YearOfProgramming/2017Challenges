# -*- coding: utf-8 -*-
#@author: Shaowen Liu


import unittest
from bst import BST, build_bst

class bst_test(unittest.TestCase):
    
    # build proper bst list
    def test_bst_build_case1(self):
        arr = [5, 2, 12, 9, 21, 3, -4, 19, 25]
        bst = build_bst(arr)
        self.assertEqual(bst.pre_order_print(), [5, 2, -4, 3, 12, 9, 21, 19, 25])
        
    def test_bst_build_case2(self):
        arr = [235, 100, 50, 700, 800, 900, 25, 75, 105, 236]
        bst = build_bst(arr)
        self.assertEqual(bst.pre_order_print(), [235,100,50,25,75,105,700,236,800,900])


    # test for delete method
    def test_bst_delete_case1(self):
        # delete the leaf node
        arr = [5, 2, -4, 3, 12, 9, 21, 19, 25]
        bst = build_bst(arr)
        bst.delete(25)
        self.assertEqual(bst.pre_order_print(), [5, 2, -4, 3, 12, 9, 21, 19])
    
    def test_bst_delete_case2(self):
        # delete the roof node
        arr = [5, 2, -4, 3, 12, 9, 21, 19, 25]
        bst = build_bst(arr)
        bst.delete(5)
        self.assertEqual(bst.pre_order_print(), [9, 2, -4, 3, 12, 21, 19, 25])
        
    def test_bst_delete_case3(self):
        # delete the node in the middle of the tree
        bst_list = [5, 2, -4, 3, 12, 9, 21, 19, 25]
        bst = build_bst(bst_list)
        bst.delete(2)
        self.assertEqual(bst.pre_order_print(), [5, 3, -4, 12, 9, 21, 19, 25])

    def test_bst_delete_case4(self):
        # delete the node in the middle of the tree
        arr = [5, 2, -4, 3, 12, 9, 21, 19, 25]
        bst = build_bst(arr)
        bst.delete(12)
        self.assertEqual(bst.pre_order_print(), [5, 2, -4, 3, 19, 9, 21, 25])       
        


if __name__ == '__main__':
    unittest.main()
