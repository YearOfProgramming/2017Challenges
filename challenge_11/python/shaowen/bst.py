# -*- coding: utf-8 -*-
# @author: Shaowen Liu

class Node():
    
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        
    def __str__(self):
        return str(self.key)
        
    def has_any_child(self):
        return self.left or self.right
    
    def the_only_child(self):
        """if the node has only one child, return the child
        else, return False
        """
        if self.left and (not self.right):
            return self.left
        elif self.right and (not self.left):
            return self.right
        else:
            return False
    
    def is_left_child(self):
        return bool(self.parent.left == self)
    
    def is_right_child(self):
        return bool(self.parent.right == self)
            
class BST():
    
    def __init__(self, root = None, size = 0):
        self.root = root
        self.size = size
    
    def _insert(self, key, current_node):
        
        if key == current_node.key:
            raise IndexError('Find duplicated key.')
        elif key > current_node.key:
            if current_node.right:
                self._insert(key, current_node.right)
            else:
                current_node.right = Node(key, parent = current_node)
        elif key < current_node.key:
            if current_node.left:
                self._insert(key, current_node.left)
            else:
                current_node.left = Node(key, parent = current_node)
        
    def insert(self, key):
        """insert new key into bst"""
        # if bst does not exist, make new node the root
        if not self.root:
            self.root = Node(key, parent = None)
        # else insert the node into bst recercively
        else:
            self._insert(key, self.root)
        self.size += 1
    
    def _has_key(self, key, current_node):
        
        if key == current_node.key:
            return current_node
        # lookup right branch
        elif key > current_node.key:
            return self._has_key(key, current_node.right)
        # lookup left branch
        elif key < current_node.key:
            return self._has_key(key, current_node.left)
        
    def has_key(self, key):
        """lookup key in bst,
        return node if key found, else False
        """
        if not self.root: 
            return False
        else:
            return self._has_key(key, self.root)
    
    def smallest_key(self, current_node):
        """start from current_node,
        search the node with the minimum key in bst
        """
        if not current_node:
            raise IndexError('this is an empty (sub)tree')
        
        if current_node.left:
            return self.smallest_key(current_node.left)
        else:
            return current_node
        
    def _delete(self, removed_node):
        
        # if removed_node has no child
        if not removed_node.has_any_child():
            # removed node is a leaf
            if removed_node.parent:
                if removed_node.is_left_child():
                    removed_node.parent.left = None
                else:
                    removed_node.parent.right = None
                self.size -= 1
            # removed node is root 
            else:
                self.root = None
                self.size = 0
                
        # removed node has only one child
        elif removed_node.the_only_child():
            if removed_node.parent:
                if removed_node.is_left_child():
                    removed_node.parent.left = removed_node.the_only_child()
                    removed_node.the_only_child().parent = removed_node.parent
                else:
                    removed_node.parent.right = removed_node.the_only_child()
                    removed_node.the_only_child().parent = removed_node.parent
            # removed node is root
            else:
                self.root = self.root.the_only_child()
        
        # removed node has two children
        else:
            min_node = self.smallest_key(removed_node.right)
            removed_node.key = min_node.key
            self._delete(min_node) 
            
    def delete(self, key):
        """delete key from bst"""
        removed_node = self.has_key(key)
        # if bst has the key, kick off delete process
        if removed_node:
            self._delete(removed_node)
        else:
            raise ValueError('key not found.')
    
    def _pre_order(self, current_node):
        
        arr = []
        arr.append(current_node.key)
        if current_node.left:
            arr += self._pre_order(current_node.left)
        if current_node.right:
            arr += self._pre_order(current_node.right)
        return arr
        
    def pre_order_print(self):
        """print the tree by pre_order traversal"""
        if self.root:
            return self._pre_order(self.root)
        else:
            return []

def build_bst(arr):
    """build a bst from an array"""
    bst = BST()
    for i in arr:
        bst.insert(i)
    return bst

if __name__ == '__main__':
    #user input
    node_arr = raw_input('Please type in a list of node integer, seperated by space.\n')
    # insert nodes
    bst = build_bst(map(int, node_arr.split()))
        
    # pre_order print
    print 'Original bst list: \n %s\n' % str(bst.pre_order_print())
    erase_keys = raw_input('Please type in key(s) you want to delete:\n')
    
    # check whether input is valid
    try:
        keys = map(int, erase_keys.split())
    except ValueError:
        raise ValueError('invalid input')
        
    # check if key exists.
    for key in keys: 
        if bst.has_key(key):
            bst.delete(key)
        else:
            print 'key %s not found.' % key
            
    print 'New bst list:\n%s\n' % str(bst.pre_order_print())  