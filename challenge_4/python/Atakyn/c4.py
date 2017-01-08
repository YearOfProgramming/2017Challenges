# invert a binary tree


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def print_tree(root):
    if root is not None:
        print_tree(root.left)
        print(root.value)
        print_tree(root.right)


def reverse(root):
    if root:
        root.left, root.right = root.right, root.left
        reverse(root.left)
        reverse(root.right)
    return root

root1 = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
print_tree(reverse(root1))
