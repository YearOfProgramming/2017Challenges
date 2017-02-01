from TreeNode import TreeNode

class Tree:

    def __init__(self,root):
        self._root = root

    def invert(self):
        return ''

    def get_root(self):
        return self._root

    def insert(self,value,node):
        if value >= node.get_value():
            if node.get_right_child() == None:
                node.set_right_child(TreeNode(value))
            else:
                self.insert(value,node.get_right_child())
        else:
            if node.get_left_child() == None:
                node.set_left_child(TreeNode(value))
            else:
                self.insert(value,node.get_left_child())

    def print_tree(self):
        self.get_root().print_node()

    def invert_tree(self):
        self.get_root().invert_node()