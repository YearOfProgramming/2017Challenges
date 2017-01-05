__author__ = "Loran425"


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def reverse(self, recursive=False):
        temp = self.left
        self.left = self.right
        self.right = temp
        if recursive:
            if self.left:
                self.left.reverse(recursive=True)
            if self.right:
                self.right.reverse(recursive=True)

    def max_depth(self):
        if self.left and self.right:
            return max(self.left.max_depth(), self.right.max_depth()) + 1
        elif self.left and not self.right:
            return self.left.max_depth() + 1
        elif self.right and not self.left:
            return self.right.max_depth() + 1
        elif not self.right and not self.left:
            return 1

    def __str__(self, depth=0):
        return str(self.value)

if __name__ == '__main__':

    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    # Single Line Equivalent
    # root = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))

    print(str(root).center(7))
    print(' '.join([str(root.left), str(root.right)]).center(7))
    print(root.left.left, root.left.right, root.right.left, root.right.right)

    print()
    root.reverse(recursive=True)

    print(str(root).center(7))
    print(' '.join([str(root.left), str(root.right)]).center(7))
    print(root.left.left, root.left.right, root.right.left, root.right.right)
