#!/usr/bin/env python3


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """
        Represent tells the computer how this class should look when printed
        :return: The printing of this class depends on the data.
        """
        return str(self.data)


def reverse_tree(node: Node):
    """
    Reverses a given Binary Tree
    :param node: The root of the binary tree
    :return: The root of the new (reversed) binary tree
    """

    # Create a variable to store the reference to node.left so it is not lost
    # When we set it to node.right
    temp = node.left
    node.left = node.right
    node.right = temp

    if node.left is not None:
        # Go through the tree recursively, swapping all referenes to child nodes
        node.right = reverse_tree(node.left)
    if node.right is not None:
        node.left = reverse_tree(node.right)

    return node


def create_nodes():
    """
    Constructs a tree of any size.
    :return: The head of the newly created tree
    """
    head = Node(1)

    # We create a queue in order to perform Breadth First Search https://en.wikipedia.org/wiki/Breadth-first_search
    # Because we need to deque the head in order to access all other parts of the tree,
    # the head is the first object in the queue
    q = [head]
    i = 1

    nodes_to_create = 200 # Change if you want to create a different number of nodes
    while i <= nodes_to_create:
        node = q[0]
        q.remove(node)

        i += 1
        node.left = Node(i)
        q.append(node.left)

        i+=1
        node.right = Node(i)
        q.append(node.right)

    return head

if __name__ == '__main__':
    root = create_nodes()
    reversed_root = reverse_tree(root)

    # testing. Only use these if you have a lot of nodes.

    print(root.left == reversed_root.right)
    print(root.left.left == reversed_root.right.right)
    print(root.left.right == reversed_root.right.left)
    print(root.left.left.left == reversed_root.right.right.right)
    print(root.left.left.right == reversed_root.right.right.left)
    print(root.left.right.left == reversed_root.right.left.right)
    print(root.left.right.right == reversed_root.right.left.left)
    print(root.right.left.left == reversed_root.left.right.right)
    print(root.right.left.right == reversed_root.left.right.left)
    print(root.right.right.left == reversed_root.left.left.right)
    print(root.right.right.right == reversed_root.left.left.left)