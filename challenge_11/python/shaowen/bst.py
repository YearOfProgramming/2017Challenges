# -*- coding: utf-8 -*-
# @author: Shaowen Liu

class Node():
    
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)
    
    def has_child(self):
        """return True, if the node has at least one child"""
        return self.left or self.right
    
    def has_one_child(self):
        """if the node has only one child, return the child
        else, return False
        """
        if self.left and (not self.right):
            return self.left
        elif self.right and (not self.left):
            return self.right
        else:
            return False
            
def has_key(root, key):
    """lookup node obj in bst, it's possible node is not in bst
    but return a 'theory' or 'should-be' path to the node anyway
    """
    if not root: return False
        
    # node found to be root
    if key == root.data:
        return True
    # lookup right branch
    elif key > root.data:
        return has_key(root.right, key)
    # lookup left branch
    elif key < root.data:
        return has_key(root.left, key)
    
def delete_node(root, key):
    """delete the node with data = key, from bst starts from root node
    args:
        root, bst node obj
        key, integer
    """
    # if root does not have key, return the original bst
    if not has_key(root, key):
        return root
        
    if root.data == key:
        # if root does not have child, delete the root directly
        if not root.has_child():
            return None
        # if root has only one child, make that child the root
        elif root.has_one_child():
            return root.has_one_child()
        # if root has two children, replace the root with the smallest node 
        # in right branch 
        else:
            min_key = smallest_key(root.right)
            root.right = delete_node(root.right, min_key)
            root.data = min_key
            return root

    # check left branch
    if root.left:
        root.left = delete_node(root.left, key)
        
    # check right branch
    if root.right:
        root.right = delete_node(root.right, key)

    return root

def insert(root, node):
    """insert a new node obj into bst starts from root"""
    # if no bst exist, make new node as root
    if root is None:
        root = node
    else:
        # add node to the right branch recursively
        if node.data >= root.data:
            root.right = insert(root.right, node)
        # add node to the left branch recersively
        else:
            root.left = insert(root.left, node)
    return root
            
def smallest_key(root):
    """return the minimum key in bst"""
    if root.left:
        return smallest_key(root.left)
    else:
        return root.data

def build_bst(arr):
    """build a bst from an array
    args:
        arr, a list of integer
    """
    root = None
    for i in arr:
        root = insert(root, Node(i))
    return root

      
def pre_order(root):
    """print the tree by pre_order traversal"""
    arr = []
    if root:
        arr.append(root.data)
        arr += pre_order(root.left)
        arr += pre_order(root.right)
    else:
        return arr
    return arr


if __name__ == '__main__':
    #user input
    node_arr = raw_input('Please type in a list of node integer, seperated by space.\n')
    # insert nodes
    root = build_bst(map(int, node_arr.split()))
        
    # pre_order print
    print 'Original bst list: \n %s\n' % str(pre_order(root))
    erase_key = raw_input('Please type in one node integer you want to delete:\n')
    
    # check whether input is valid
    try:
        erase_key = int(erase_key)
    except ValueError:
        raise ValueError('invalid input')
    # check if key exists.
    if has_key(root, erase_key):
        root = delete_node(root, erase_key)
        print 'New bst list:\n%s\n' % str(pre_order(root))
    else:
        print 'key not found.'
    
    
            

    
    
        
        
        