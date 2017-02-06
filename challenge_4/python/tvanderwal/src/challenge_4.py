#Challenge 4: Take a binary tree and reverse it
#I decided to create two classes. One to hold the node, and one to act as the Binary Tree.

#Node class
#Only contains the information for the node. Val is the value of the node, left is the left most value, and right is the right value
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

#BinaryTree class
class BinaryTree:
    #Initialize the tree with a  blank root
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    #Recursively add node objects
    def add(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    #Recursively print each node in the tree
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(node.val)
            self._printTree(node.right)

    #returns a nested list of each level and the nodes in it
    def getTree(self):
        currLevel = [self.root]
        tree = list()
        while currLevel:
            lowerLevel = list()
            currNodes = list()
            for node in currLevel:
                currNodes.append(node.val)
                if node.left:
                    lowerLevel.append(node.left)
                if node.right:
                    lowerLevel.append(node.right)
            tree.append(currNodes)
            #print(currNodes)
            currLevel = lowerLevel
        return tree



if __name__ == '__main__':
    #create sample tree from example
    tree = BinaryTree()
    tree.add(4)
    tree.add(2)
    tree.add(7)
    tree.add(1)
    tree.add(3)
    tree.add(6)
    tree.add(9)

    #getTree returns the tree formatted in nested lists
    formattedTree = tree.getTree()
    #reverse the levels
    for level in formattedTree:
        level.reverse()
        print(level)