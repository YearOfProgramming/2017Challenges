Random Pointer Linked List
======
List nodes will be arrays: [data, random-node, next-node]
Algo:
Iterate through the linked list mapping random pointers to the node that owns them
and mapping old nodes to corresponding new nodes.
Create new list as you iterate through the original list.

If a random pointer points to a previously seen node, point current new node
to previous new node in mapping from old nodes.

If a random pointer points to a non-previously seen node, map unknown node to current new node.  
If current old node maps to previous new node, point current new node's random pointer
