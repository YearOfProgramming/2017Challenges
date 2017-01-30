from TreeNode import TreeNode

class Tree:

    def __init__(self,root):
        self.root = root

    def invert(self):
        return ''

    def GetRoot(self):
        return self.root

    def insert(self,value,node):
        if value >= node.GetValue():
            if node.GetRightChild() == None:
                node.SetRightChild(TreeNode(value))
            else:
                self.insert(value,node.GetRightChild())
        else:
            if node.GetLeftChild() == None:
                node.SetLeftChild(TreeNode(value))
            else:
                self.insert(value,node.GetLeftChild())

    def printTree(self):
        self.GetRoot().printNode()