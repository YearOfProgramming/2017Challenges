#!/usr/bin/env python3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


def deep_copy(root: Node) -> Node:
    # A dictionary linking the data of the roots nodes to the memory address of the new (copied) nodes
    old_to_new = {}

    # A temporary pointer to the root of the list
    temp = root

    # This is how you iterate through a linked list
    # Iterate through the list and map original nodes to their copies
    while temp is not None:
        old_to_new[temp.data] = Node(temp.data + '\'')
        temp = temp.next

    temp = root
    while temp.next is not None:
        # Get the node we are about to set from the list
        node = old_to_new[temp.data]
        # Set the next value as well so that it is taken care of when we move to the next node
        node.next = old_to_new[temp.next.data]
        if temp.random is not None:
            # If the random pointer exists, set it for this node.
            node.random = old_to_new[temp.random.data]
        # Keep going through the linked list, whereas for every node we are also
        # accessing a different part of the dictionary
        temp = temp.next

    return old_to_new[root.data]


if __name__ == '__main__':


    print(n.next.data == new.next.data[:1])
    print(new.next.random == new.next.next.next.next)
    print(new.next.next.next.random == new)