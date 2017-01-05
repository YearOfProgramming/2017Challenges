First you must make your tree.


treeObj.addNode(val) makes a node with the value (val) assigned to it.
The first Node you enter becomes the root.
Any following nodes will be put in the place they would be in a BST (as it is one).


treeObj.deleteTree() deletes the root, and therefor the whole tree


treeObj.getRoot() returns the root node.


treeObj.searchTree(val) returns the Node with the value (val).


The suffix .r (used on the 3rd and 4th commands) returns the right node of the one specified (ex: "treeObj.getRoot().r" will return the node right of the root).

The suffix .l (used on the 3rd and 4th commands) returns the left node of the one specified (ex: "treeObj.getRoot().l" will return the node left of the root).

.r and .l can be stacked (ex:"treeObj.getRoot().r.r" will return the right node of the right node of the root).

The suffix .v will return the value of the specified node (ex: If the Root node has a value of 5, "treeObj.getRoot().v" will return 5)


Using that you will be able to make your Tree and comfirm it's how you want it.


To reverse the tree, it's simple reverseTree(treeObj.getRoot())

After executing that function, your tree will be reversed. Comfirm this by looking through the nodes using the functions from above.