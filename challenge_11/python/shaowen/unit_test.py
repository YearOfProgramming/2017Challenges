# -*- coding: utf-8 -*-
#@author: Shaowen Liu


import unittest
import bst
from bst import Node

class bst_test(unittest.TestCase):
    
    # build proper bst list
    def test_bst_build_case1(self):
        arr = [5, 2, 12, 9, 21, 3, -4, 19, 25]
        root = bst.build_bst(arr)
        self.assertEqual(bst.pre_order(root), [5, 2, -4, 3, 12, 9, 21, 19, 25])
        
    def test_bst_build_case2(self):
        arr = [235, 100, 50, 700, 800, 900, 25, 75, 105, 236]
        root = bst.build_bst(arr)
        self.assertEqual(bst.pre_order(root), [235,100,50,25,75,105,700,236,800,900])


    # test for delete method
    def test_bst_delete_case1(self):
        # delete the leaf node
        bst_list = [5, 2, -4, 3, 12, 9, 21, 19, 25]
        root = bst.build_bst(bst_list)
        root = bst.delete_node(root,25)
        self.assertEqual(bst.pre_order(root), [5, 2, -4, 3, 12, 9, 21, 19])
    
    def test_bst_delete_case2(self):
        # delete the roof node
        bst_list = [5, 2, -4, 3, 12, 9, 21, 19, 25]
        root = bst.build_bst(bst_list)
        root = bst.delete_node(root,5)
        self.assertEqual(bst.pre_order(root), [9, 2, -4, 3, 12, 21, 19, 25])
        
    def test_bst_delete_case3(self):
        # delete the node in the middle of the tree
        bst_list = [5, 2, -4, 3, 12, 9, 21, 19, 25]
        root = bst.build_bst(bst_list)
        root = bst.delete_node(root,2)
        self.assertEqual(bst.pre_order(root), [5, 3, -4, 12, 9, 21, 19, 25])

    def test_bst_delete_case4(self):
        # delete the node in the middle of the tree
        bst_list = [5, 2, -4, 3, 12, 9, 21, 19, 25]
        root = bst.build_bst(bst_list)
        root = bst.delete_node(root,12)
        self.assertEqual(bst.pre_order(root), [5, 2, -4, 3, 19, 9, 21, 25])       
        


if __name__ == '__main__':
    unittest.main()
