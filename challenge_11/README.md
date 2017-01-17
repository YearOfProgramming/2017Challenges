Removing a Node from a BST
======
Idea
------
Binary Trees are a big deal in computer science. It's only fitting that we have a couple challenges that utilize them. The purpose of this assignment is to create a function capable of removing a node from a [Binary Search Tree](https://en.wikipedia.org/wiki/Binary_search_tree). Every node should have a left, right and data attribute. Left and right will eventually be set to either another Node or null/None, the data attribute will be an int. Along with removing a node from a binary search tree, you should also have a function that prints the tree out in pre-order (mostly for testing purposes). 
 
 A few other functions that might be helpful
 * findSmallest - finds and returns the node with the smallest data value
 * findLargest - finds and returns the node with the largest data value
 * insert - inserts a node into the BST, mostly useful for testing.
 
 [Testing](https://github.com/YearOfProgramming/2017Challenges#testing)
 -----
 Testing for this challenge is fairly straight forward. Simply insert a bunch of nodes into the BST, remove one then print the BST to ensure that it was removed.
 
 Notes:
 * Please implement functionality to read standard input. Upon activating the program the user should be prompted with a message asking them to input space separated values (lets say characters) which are to be put inserted into the tree one after the other. These values will not repeat.
 * The tree should now be printed in pre-order
 * A new prompt should appear asking what value(s) the user would like to delete from the tree. This input will be space seperated and non repeating.
 * The program should output the tree again, in pre order then terminate.
 
 ##### Testing with the test script
 
 You will receive a few values line by line:
 
 1. `i#` where `i` means to insert the `#` (e.g. `i24`).
 2. `d#` where `d` means to delete the node with the `#` (e.g. `d24`).
 3. `oin`, `opre`, `opost`, where the `o` means output and `in` means print out in order, `pre` means preorder, and `post`, means post order.
 4. `e` means to stop end.
 
 Look at the `testfiles/` directory to look at the testfiles.
 
 
Example:
 
    i2
    i3
    oin
    opre
    d2
    e
  
This means to insert 2, insert 3, print out in order, print out pre order, delete 2, and end your program.

Expected output:

    2
    3
    2
    3
