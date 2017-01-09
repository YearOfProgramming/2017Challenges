#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BTree:
    def __init__(self, value, left=None, right=None):
        self.root = Node(value)
        self.root.left = left
        self.root.right = right

    def get_root(self):
        return self.root

    def pivot(self):
        self.root.pivot()

    def tree_print(self):
        self.root.tree_print()


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def tree_print(self, indent=0):
        """ Prints the tree hierarchically on the command line
        """
        print("{}{}".format('  ' * indent, str(self.value)))
        if self.left:
            self.left.tree_print(indent+1)
        if self.right:
            self.right.tree_print(indent+1)

    def depth(self):
        """ Calculate the max depth of the tree
        """
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.depth()
        elif self.right is None:
            return 1 + self.left.depth()
        else:
            return 1 + max(self.left.depth(), self.right.depth())


def flip_tree(node):
    """ Flips the tree by pivoting the children from bottom to top
    """
    # Get the root node of tree, only executes once
    if hasattr(node, "root"):
        node = node.get_root()

    if node.left:
        flip_tree(node.left)
    if node.right:
        flip_tree(node.right)
    node.left, node.right = node.right, node.left
