# DeepCopy

The solution is as follows.

Each element in the linked list will hold 5 variables:
    the value of the root
    its place in the linked list (0 for the last element, N-1 for the first element)
    the next list
    the random list
    a `current` to remember it's place in its iterator


This way, given the root of a linked list, I am able to iterate through that list and obtain the value of the root of every element. I then make a RandomPointerLinkedList object each holding that root and slowly build it up. The index that each linkedlist holds will tell me where to have the random linked list point to (rather than constantly searching). 
