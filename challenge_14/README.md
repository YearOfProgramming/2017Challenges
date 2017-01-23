Reversing a linked list
======
Idea
----
Everyone should be somewhat familiar with the concept of a linked list by now. Today, you're job is to create a linked list and reverse it. Your program needs to be able to take strings from standard input, which will be used as each nodes data attribute. The strings in standard input will be space separated. Nodes are to be created and connected for these strings one after another (newest node is appended to the end of the linked list). 

As for the "reverse" function. You need to implement a function to reverse the linked list. However, you may not touch the data on any of the nodes. The list must be reversed by manipulating the "next" attribute of each node. 

The program should run in O(N) time.

You should have another function that will print the linked list (simply loop through it and print the data at each node).  
   
Testing
------
In order to test the program, you may use the provided test files. Plug all strings from the test files into your program to create a node for each one. Print the list of nodes then reverse the list. After the list has been completely reversed output the list again (which should result in the reverse of what was previously printed). 

The test inputs are also listed below.

1. r e d r u m

2. p a r k

3. b o o b y t r a p

4. l i v e