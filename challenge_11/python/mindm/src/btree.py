#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BTree:
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
        else:
            self.root = None

    def get_root(self):
        return self.root

    def pivot(self):
        self.root.pivot()

    def tree_print(self):
        self.root.tree_print()

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)

    def pre_print(self):
        self.root.pre_print()

    def remove(self, value):
        self.root = self.root.search_remove(value)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def find_smallest(self):
        if self.left:
            return self.left.find_smallest()
        else:
            return self.value

    def find_largest(self):
        if self.right:
            return self.right.find_largest()
        else:
            return self.value

    def search_remove(self, value):
        """ Removes a vlue from the tree
        """
        if value < self.value:
            self.left = self.left.search_remove(value)
        elif value > self.value:
            self.right = self.right.search_remove(value)
        else:
            if self.right is None and self.left is not None:
                return self.left
            if self.left is None and self.right is not None:
                return self.right
            if self.left is None and self.right is None:
                return None
            self.value = self.left.find_largest()
            self.left = self.left.search_remove(self.value)
        return self

    def insert(self, value):
        """ Insert node in BST
        """
        if value < self.value:
            self.pass_left(value)
        else:
            self.pass_right(value)

    def pass_left(self, value):
        if self.left is not None:
            self.left.insert(value)
        else:
            self.left = Node(value)

    def pass_right(self, value):
        if self.right is not None:
            self.right.insert(value)
        else:
            self.right = Node(value)

    def tree_print(self, indent=0):
        """ Prints the tree hierarchically on the command line
        """
        print("{}{}".format('  ' * indent, str(self.value)))
        if self.left:
            self.left.tree_print(indent+1)
        else:
            print("{}{}".format('  ' * (indent+1), "-"))
        if self.right:
            self.right.tree_print(indent+1)
        else:
            print("{}{}".format('  ' * (indent+1), "-"))

    def pre_print(self):
        """ Prints tree in pre-order
        """
        print(self.value)
        if self.left:
            self.left.pre_print()
        if self.right:
            self.right.pre_print()

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
