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


def reverse(root):  # solution, accounts for unpaired nodes (e.g. if 10 were added to the challenge example tree)
    if root is not None:
        if root.left is not None:
            temp = root.left
            root.left = root.right
            root.right = temp
            reverse(root.left)
            reverse(root.right)
        if root.right is not None:
            temp = root.right
            root.right = root.left
            root.left = temp
    return root

root1 = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
print_tree(reverse(root1))
