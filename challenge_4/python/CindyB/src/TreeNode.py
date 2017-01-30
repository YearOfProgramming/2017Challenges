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
        
    def printNode(self):
        if self.GetLeftChild() != None:
            self.GetLeftChild().printNode()
        print str(self.GetValue()),
        if self.GetRightChild() != None:
            self.GetRightChild().printNode()

    def invertNode(self):
        if self.GetLeftChild() != None:
            self.GetLeftChild().invertNode()
        if self.GetRightChild() != None:
            self.GetRightChild().invertNode()
        tempNode = self.GetLeftChild()
        self.SetLeftChild(self.GetRightChild())
        self.SetRightChild(tempNode)