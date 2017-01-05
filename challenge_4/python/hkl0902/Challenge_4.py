class BinTree:
    '''
    Root: integer value
    Left: BinTree
    Right: BinTree
    if left and right are both None, the tree is a leaf (an ending node)
    '''
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

    '''
    Converts the Binary Tree into a list
    The first element is None.
    Each element in the list after the first is a root in the tree.
    The children of any element is at the (2i, 2[i+1]) indices

    The tree given in the README would become [None, 4, 2, 7, 1, 3, 6, 9]
    The children to (4) is located at (2, 3) or (2*1, 2*(1+1))
    The children to (2) is located at (4, 5) or (2*2, 2*(2+1))
    The children to (7) is located at (6, 7) or (2*3, 2*(3+1))
    If no child root exist, that place is replaced with None
    Used only for testing purposes
    '''
    def convertToLst(self):
        lst = [None]
        queue = [self]
        lst.append(self.root)
        # Breadth first search of BST
        while len(queue) > 0:
            v = queue.pop(0)
            i = lst.index(v.root)
            if len(lst) < 2*i:
                while (len(lst) < 2*i):
                    lst.append(None)
            if v.left:
                queue.append(v.left)
                lst.append(v.left.root)
            else:
                lst.append(None)
            if v.right:
                queue.append(v.right)
                lst.append(v.right.root)
            else:
                lst.append(None)
        return lst

    '''
    Solution to Challenge 4
    Directly modifies self

    Reverses the subtrees
    Switches the subtrees s.t. self.left = self.right, self.right = self.left
    '''
    def reverse(self):
        reversedLeft = None
        reversedRight = None
        if self.left:
            reversedLeft = self.left.reverse()
        if self.right:
            reversedRight = self.right.reverse()
        self.left = reversedRight
        self.right = reversedLeft
        return self

leaf1 = BinTree(1, None, None)
leaf2 = BinTree(3, None, None)
leaf3 = BinTree(6, None, None)
leaf4 = BinTree(9, None, None)

leftTree = BinTree(2, leaf1, leaf2)
rightTree = BinTree(7, leaf3, leaf4)

tree = BinTree(4, leftTree, rightTree)
print(tree.convertToLst())
tree.reverse()
print(tree.convertToLst())
