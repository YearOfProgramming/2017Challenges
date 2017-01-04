# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # If there is no root, return Nothing
        if root == None:
            return None
        # We can save a depth of the recursion if we stop before we get outside the leaf
        if root.left == None and root.right == None:
            return root
            
        # Switch the left and right pointers
        temp = root.left
        root.left = root.right
        root.right = temp
        # Recursively call the function for left and right branches
        self.invertTree(root.left)
        self.invertTree(root.right)
        # Return the root of the inverted tree
        return root