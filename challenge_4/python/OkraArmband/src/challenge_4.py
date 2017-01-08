class BinaryTree():
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def invertTree(self):
        """
        Swap left and right children of input BinaryTree for all subsequent children as well (recursively).
        """
        temp = self.left
        self.left = self.right
        self.right = temp


        # Continue the recursion as long as we haven't reached the end of a branch
        if self.left is not None:
            self.left.invertTree()
        if self.right is not None:
            self.right.invertTree()

    @classmethod
    def from_list(cls,data):
        """
        :type DATA: list
        :rtype: BinaryTree

         Uses recursion to create a BinaryTree instance from a list: data.
         Note that "data" can be a list containing lists, i.e. [4,[2,1,3]]. However, for a left or right child in the
         tree that contains no value, "None" must be passed in: [4,None,7], for example.
        """
        try: # Run this block if "data" is a list of 3 things
            root = cls(data[0])
            if data[1] is not None:
                root.left = cls.from_list(data[1])
            if data[2] is not None:
                root.right = cls.from_list(data[2])
        except TypeError: # If "data" passed in is None
            root = cls(data)
        return root

    def printTree(self):
        if self.left is not None:
            self.left.printTree()
        if self.root is not None:
            print(self.root)
        if self.right is not None:
            self.right.printTree()

