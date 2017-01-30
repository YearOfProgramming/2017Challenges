import sys

from Tree import Tree
from TreeNode import TreeNode

input = [4,2,7,1,3,6,9]
myTree = Tree(TreeNode(input[0]))
input.remove(input[0])

for value in input:
    myTree.insert(value,myTree.GetRoot())