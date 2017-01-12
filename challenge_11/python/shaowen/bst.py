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
    """lookup key in bst,
    return Ture if key found, else False
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
    """delete the node with data equals to key.
    args:
        root, bst node obj
        key, int
    """
    # if root does not have key, return the root directly
    if not has_key(root, key):
        return root
        
    # check root    
    if root.data == key:
        # if root does not have child, delete the root directly
        if not root.has_child():
            return None
        # if root has only one child, make that child the root
        elif root.has_one_child():
            return root.has_one_child()
        # if root has two children, 
        # 1. replace the root with the smallest key in right branch
        # 2. delete that node with the smallest key
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

def insert(root, key):
    """insert a new node obj into bst
    args:
        root, node obj
        key, int
    
    """
    new_node = Node(key)
    # if bst does not exist, make new node the root
    if root is None:
        root = new_node
    else:
        # add node to the right branch recursively
        if key >= root.data:
            root.right = insert(root.right, key)
        # add node to the left branch recersively
        else:
            root.left = insert(root.left, key)
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
        root = insert(root, i)
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
    erase_keys = raw_input('Please type in key(s) you want to delete:\n')
    
    # check whether input is valid
    try:
        keys = map(int, erase_keys.split())
    except ValueError:
        raise ValueError('invalid input')
        
    # check if key exists.
    for key in keys: 
        if has_key(root, key):
            root = delete_node(root, key)
            #print 'key %s is deleted from bst' % key
        else:
            print 'key %s not found.' % key
            
    print 'New bst list:\n%s\n' % str(pre_order(root))  