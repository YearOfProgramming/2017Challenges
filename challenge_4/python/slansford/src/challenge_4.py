
#Constructs Node-class objects, "branches" of the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Constructs Binary Tree object, defines structure of Node objects
class bTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
        else:
            self._add(node, value, self.root)

    def _add(self, node, value, parent):
        if value == None:
            return 
        elif value <= parent.value:
            if parent.left == None:
                parent.left = node
            else:
                self._add(node, value, parent.left)
        else:
            if parent.right == None:
                parent.right = node
            else:
                self._add(node, value, parent.right)


#Inverts nodes of bTree-class object
def invert(node):
    toLeft = node.right
    toRight = node.left
    node.left = toLeft
    node.right = toRight
    if node.left is not None:
        invert(node.left)
    if node.right is not None:
        invert(node.right)


#Constructing the tree
tree = bTree()
tree.add(4)
tree.add(2)
tree.add(1)
tree.add(3)
tree.add(7)
tree.add(6)
tree.add(9)


#Prints value for specific branch of tree
print(tree.getRoot().left.right.value)

invert(tree.getRoot())

print(tree.getRoot().left.right.value)