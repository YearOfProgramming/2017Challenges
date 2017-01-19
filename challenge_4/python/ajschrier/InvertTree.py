class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def nodeDepth(root):
    # Empty tree
    if root is None:
        return 0
    # Node only
    elif root.left is None and root.right is None:
        return 1
    # One sided trees
    elif root.left is None:
        return 1 + nodeDepth(root.right)
    elif root.right is None:
        return 1 + nodeDepth(root.left)
    # Two sided trees
    else:
        return 1 + (max(nodeDepth(root.left), nodeDepth(root.right)))


def flipTree(root):
    # Return none if root is none
    if root is None:
        return None
    # Return if there are no leaves
    if root.left is None and root.right is None:
        return root
    # Perform the flip
    root.left, root.right = root.right, root.left
    # Recur for the leaves
    flipTree(root.left)
    flipTree(root.right)
    return root


def treePrint(root, level=0):
    # Adds a prefix for indentation
    prefix = '-' * level
    if root is None:
        return
    print "{}{}".format(prefix, root.value)
    treePrint(root.left, level + 1)
    treePrint(root.right, level + 1)


def main():
    T = Node(4,
             Node(2,
                  Node(1),
                  Node(3)),
             Node(7,
                  Node(6),
                  Node(9)))
    treePrint(T)
    print "Here we goo......"
    treePrint(flipTree(T))


if __name__ == '__main__':
    main()
