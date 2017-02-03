from TreeNode import TreeNode

class Tree:

    def __init__(self,root):
        self._root = root

    def insert(self,value):
        self._insert(value,self._root)

    def _insert(self,value,node):
        if value >= node._value:
            if node._right_child == None:
                node._right_child = TreeNode(value)
            else:
                self._insert(value,node._right_child)
        else:
            if node._left_child == None:
                node._left_child = TreeNode(value)
            else:
                self._insert(value,node._left_child)

    def print_tree(self):
        self._root.print_node()

    def invert_tree(self):
        self._root.invert_node()