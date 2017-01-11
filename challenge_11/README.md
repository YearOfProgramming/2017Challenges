Removing a Node from a BST
======
Idea
------
Binary Trees are a big deal in computer science. It's only fitting that we have a couple challenges that utilize them. The purpose of this assignment is to create a function capable of removing a node from a [Binary Search Tree](https://en.wikipedia.org/wiki/Binary_search_tree). Every node should have a left, right and data attribute. Left and right will eventually be set to either another Node or null/None, the data attribute will be an int. Along with removing a node from a binary search tree, you should also have a function that prints the tree out in pre-order (mostly for testing purposes). 
 
 A few other functions that might be helpful
 * findSmallest - finds and returns the node with the smallest data value
 * findLargest - finds and returns the node with the largest data value
 * insert - inserts a node into the BST, mostly useful for testing.
 
 Testing
 -----
 Testing for this challenge is fairly straight forward. Simply insert a bunch of nodes into the BST, remove one then print the BST to ensure that it was removed.