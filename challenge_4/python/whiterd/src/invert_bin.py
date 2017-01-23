#!/usr/bin/env python

'''
    Input:  An object consisting of a binary tree.

    Output:  The same tree with values mirrored.
'''

def mirror(node):
    if node:
        mirror(node.left)
        mirror(node.right)
        node.left, node.right = node.right, node.left
        
    return node
