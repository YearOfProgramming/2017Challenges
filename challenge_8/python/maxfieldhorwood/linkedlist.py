
class LinkedList(object):
    
    def __init__(self, data):
        self.data = data
        self.nxt = None
        self.root = None

    def assignRoot(self):
        self.root = self
        
    def insertNode(self, data):
        tempR = self
        newNode = LinkedList(data)
        while tempR.nxt is not None:
            tempR = tempR.nxt
        tempR.nxt = newNode

    def display(self):
        tRoot = self.root
        while tRoot is not None:
            print(tRoot.data)
            tRoot = tRoot.nxt
        
def deepCopy(r):
    linkedCopy = LinkedList(r.data+" '")
    linkedCopy.assignRoot()
    tRoot = r.nxt # Ignore first root
    while tRoot is not None:
        data = tRoot.data+" '"
        linkedCopy.insertNode(data)
        tRoot = tRoot.nxt
    return linkedCopy

root = LinkedList("0")

root.assignRoot()

root.insertNode("1")
root.insertNode("2")

rootCopy = deepCopy(root)

root.display()
rootCopy.display()


root.insertNode("4")
rootCopy.insertNode("4 '")

root.display()
rootCopy.display()
