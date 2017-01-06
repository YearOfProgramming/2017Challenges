class Node:
    """
    Binary tree node structure.
    """
    def __init__(self, value, left=None, right=None):
        self.right = right  #define right node
        self.left = left    #define left node
        self.value = value  #define value of current node

def invert_tree(root):
    """
    Inverts a binary tree.
    """
    #if no node here, nothing to invert
    if root == None:
        return None
    
    #otherwise, exchange left and right branches
    temp = root.right
    root.right = root.left
    root.left = temp
    
    #repeat for each branch using recursion
    invert_tree(root.left)
    invert_tree(root.right)
    return root

#print tree.
#thanks to @kokimame for this cool tree visualization idea!
#see his implementation in C here: challenge_4/c/kokimame/invertTree.c
#to use: 
#   define a spacer (e.g. "" for root node), 
#   the node to be visualized (e.g. tree1 for root of tree1), 
#   and the direction of the node (e.g. "center" for root node).
def print_tree(spacer, root, dir):   
    spacer = spacer + "    "                #spacer used to align printed branches
    if root == None:
        return                              #end when no more nodes to traverse
    print_tree(spacer, root.right, "right") #right nodes are printed first
    if dir == "right":
        print(spacer, "/ ", root.value)     #right branches marked with /
    if dir == "center":
        print(spacer + "   ", root.value)   #center branch printed next, no mark
    if dir == "left":
        print(spacer, "\\ ", root.value)    #left branches marked with \
    print_tree(spacer, root.left, "left")   #left nodes are printed last


#symmetrical tree:
tree1 = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
print("tree1 before:")
print_tree("", tree1, "center")
invert_tree(tree1)
print("tree1 after:")
print_tree("", tree1, "center")

#asymmetrical tree:
tree2 = Node(9, Node(8, Node(3)), Node(7, Node(6), Node(4)))
print("tree2 before:")
print_tree("", tree2, "center")
invert_tree(tree2)
print("tree2 after:")
print_tree("", tree2, "center")
