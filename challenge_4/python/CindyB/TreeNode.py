class TreeNode:

    def __init__(self,value):
        self.value = value
        self.rightChild = None
        self.leftChild = None

    def GetValue(self):
        return self.value

    def SetRightChild(self,child):
        self.rightChild = child

    def SetLeftChild(self,child):
        self.leftChild = child

    def GetRightChild(self):
        return self.rightChild
    
    def GetLeftChild(self):
        return self.leftChild