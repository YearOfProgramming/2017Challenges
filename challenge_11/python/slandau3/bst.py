#!/usr/bin/env python3
# @author slandau3
import random


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(data, root):
    """
    Inserts a node into the tree.
    :param data: The data which will be given to the inserted node
    :param root: The root of the tree
    :return: The new root of the tree, with a new node inserted
    """
    if root is None:
        return Node(data)
    elif data > root.data:
        root.right = insert(data,root.right)
    elif data < root.data:
        root.left = insert(data,root.left)

    return root


def createTree(num_nodes):
    """
    A function created to construct the tree from 0 to num_nodes
    The root will be the the middle number of num_nodes
    :param num_nodes: The number of nodes to create in the list
    :return: The root of the newly assembled tree
    """
    root = Node(num_nodes//2)

    for i in range(num_nodes):
        if i == num_nodes//2:
            continue

        root = insert(i, root)
    return root


def printPreOrder(root):
    """
    Prints the tree in preorder
    :param root: The root of the tree
    :return: None
    """
    if root is None:
        return
    print(root.data)
    printPreOrder(root.left)
    printPreOrder(root.right)


def remove(root, data):
    if root is None:
        return root
    elif data < root.data:
        # If the data is less than that of the current node
        # We know we have to look to the left
        root.left = remove(root.left, data)
    elif data > root.data:
        # If the data is greater than that of hte current node
        # we know that we have to look to the right
        root.right = remove(root.right, data)
    elif data == root.data:
        # We have found the node we are looking for
        # In order to solve this problem the node we are removing (assuming its a non leaf node)
        # will need to be replaced with something. After some experimenting and soul searching
        # you will see that the node we need to replace it with is the closest node to what it was.
        # In other words we need the largest node in the left sub-tree or the smallest node in the
        # Right sub-tree. We are going to worry about swapping the data only to make things a lot easier.
        if root.left is not None:
            # If we know the left subtree exists, we need to look for hte largest node in it.
            largest = findBiggest(root.left).data
        elif root.right is not None:
            # If we know the right subtree exists (which at this point means the left does not)
            # means that we need to search for the smallest value in the right subtree.
            largest = findSmallest(root.right).data
        else:
            # If the root is a leaf node then we can easily remove it
            root = None
            return root

        # Search through the list and find the largest value (which will either just remove directly
        # or cause us to remove a few others)
        root = remove(root, largest)
        root.data = largest

    return root


def findBiggest(root):
    """
    Finds the largest node in the tree
    :param root: The starting node of the subnodes you want to saerch through
    :return: The largest Node in the given subtree
    """
    if root.right is None:
        return root
    else:
        return findBiggest(root.right)


def findSmallest(root):
    """
    Finds the smallest node in the subtree
    :param root: The root node of the tree or subtree
    :return: The smallest node in the given subtree
    """
    if root.left is None:
        return root
    else:
        return findSmallest(root.left)


root = createTree(100)
#printPreOrder(root)
print('\n\n')
root = remove(root, 50)
root = remove(root, 99)
root = remove(root, 98)
root = remove(root, 0)
print('\n\n')
printPreOrder(root)

