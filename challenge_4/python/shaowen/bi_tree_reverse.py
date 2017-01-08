# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 11:01:42 2017

@author: shaowen Liu
"""

class Node():
    def __init__(self, data, left_child = None, right_child = None):
        self.data = data
        self.left = left_child
        self.right = right_child
    
    def has_child(self):
        return (self.left or self.right)
    
def bi_insert(root, new_node):
    # insert new node into the tree
    # arg 1: the root of the tree, type object
    # arg 2. the new node to be inserted, type object
    if new_node.data >= root.data:
        # insert new node to the right
        if root.right:
            bi_insert(root.right, new_node)
        else:
            root.right = new_node
    if new_node.data < root.data:
        # insert new node to the left 
        if root.left:
            bi_insert(root.left, new_node)
        else:
            root.left = new_node

def rev_tree(root):
    # reverse binary tree
    if root.has_child:
        # exchange the pos of two sub nodes 
        root.left, root.right = root.right, root.left
        # go on the recursive proc with the child
        if root.left:
            rev_tree(root.left)
        if root.right:
            rev_tree(root.right)