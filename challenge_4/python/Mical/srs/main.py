# Mical | 03/01/2017




# 1/2 This is what lets you actually make the Tree

class Node:
    def __init__(self, val): # This is the constructor for the node
        self.v = val # This sets v to the entered value
        self.r = None # This sets r (the right child) to None (the default value)
        self.l = None # This sets l (the left child) to None (the default value)

class Tree:
    def __init__(self): # This is the constructor for the Tree
        self.root = None # This sets the Root to None (the default value)

    def getRoot(self): # This gives you the root
        return self.root # Returns the Root

    def addNode(self, val): # This adds a Node to the tree 1/2
        node = Node(val) # This sets node to a Node with the value entered assigned to it
        if self.root == None: # This checks if Root does not have a Node assigned to it...
            self.root = node # ... and assigns node to it if that's true
        else:
            self._addNode(node, val, self.root) # If Root already has a Node, it calls the _addNode function

    def _addNode(self, node, val, parNode): # This adds a Node to the tree 2/2
        if val <= parNode.v: # This checks if node's value is less than or equal to the current Node's value...
            if parNode.l == None: # ... If it is and the current Node does not have a left child...
                parNode.l = node #... it assigns node to be the current Node's left child
            else: # ... If it is and the current Node has a left child...
                self._addNode(node, val, parNode.l) # ... It calls the _addNode function with the left child
        else: # If node's value is not less than or equal to the current Node's value...
            if parNode.r == None: # ... And the current node does not have a right child...
                parNode.r = node # ... It assigns node to be the current Node's right child...
            else: # ... If the current node has a right child...
                self._addNode(node, val, parNode.r) # ... It calls the _addNode function with the right child

    def searchNode(self, val): # This searches for values Nodes in the Tree and returns the Node 1/2
        if self.root == val: # This checks if Root is equal to the value being looked for...
            return self.root.v # ... If it is it returns Root
        else: # ... If not ...
            return self._searchNode(val, self.root) # ... It calls the _searchNode function

    def _searchNode(self, val, curNode): # This searches for values Nodes in the Tree and returns the Node 1/2
        if val == curNode.v: # This checks if the current node's value is equal to the value being looked for...
            return curNode # ... If it is, it returns the current node
        elif val < curNode.v: # If not, and the value being searched for is less than the current node's value...
            return self._searchNode(val, curNode.l) # ... If it is then it calls _searchNode on the left child
        else: # ... If not ...
            return self._searchNode(val, curNode.r) # ... If not it calls _searchNode on the right child

    def deleteTree(self): # This deletes the Tree
        self.root = None # By setting root to None, it deletes the Tree.




# 2/2 The following is the function that actually reverses the Tree
# While the Tree above is a BST, this function will work on any Binary Tree of any size

def reverseTree(node):  # This reverses the position of the children nodes of a node (to reverse the whole tree give it the Tree's Root)
    rightToLeft = node.r  # Stores the right child to rightToLeft
    leftToRight = node.l  # Stores the left child to leftToRight
    node.l = rightToLeft  # Sets the left child to rightToLeft
    node.r = leftToRight  # Sets the right child to leftToRight
    if node.l != None:  # Checks if there is a left child node...
        reverseTree(node.l)  # ... if there is, it calls reverseTree on it
    if node.r != None:  # Checks if there is a right child node...
        reverseTree(node.r)  # ... if there is, it calls reverseTree on it




# How to use: Tree().addNode(value) adds a node to the tree with the value given, and puts it where it belongs
#             Tree().searchNode(value) returns the Node with the value you gave it
#             Tree().deleteTree deletes/empties a tree
#             Tree().getRoot returns the Root Node

treeObj = Tree()
# This will set the tree as the same one in the example, but any tree can be used.
treeObj.addNode(4)
treeObj.addNode(2)
treeObj.addNode(1)
treeObj.addNode(3)
treeObj.addNode(7)
treeObj.addNode(6)
treeObj.addNode(9)

print(treeObj.getRoot().r.v) # Prints the value of the right child of the root node pre-reversal

reverseTree(treeObj.getRoot())

print(treeObj.getRoot().r.v) # Prints the value of the right child of the root node post-reversal
