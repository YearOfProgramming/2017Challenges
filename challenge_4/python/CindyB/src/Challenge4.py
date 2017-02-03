from Tree import Tree
from TreeNode import TreeNode

input = [4,2,7,1,3,6,9]
my_tree = Tree(TreeNode(input[0]))
input.remove(input[0])

for value in input:
    my_tree.insert(value)

my_tree.print_tree()
my_tree.invert_tree()
my_tree.print_tree()