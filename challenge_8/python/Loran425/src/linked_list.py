import random

__author__ = "Loran425"


class Node(object):
    def __init__(self, value, root=False):
        self.value = value                               # the value of the node
        self.length = 0                                  # how long is the chain used for get_rand_node
        self.next = None                                 # next node in line
        self.rand = None                                 # random previous node
        self.root = root                                 # is this the root node

    def add_node(self, value):                           # grow the chain
        self.next = Node(value)                          # were growing so make sure we know how to find the next

    def set_next(self, nxt):
        assert type(nxt) == Node                         # next node can only be a node
        self.next = nxt                                  # set it up

    def set_rand(self, root, node=None):
        if self.root:                                    # root cant have a back link
            return

        node_set = False                                 # watchdog variable
        if not node:                                     # set a random node if none is given
            while not node_set:                          # this verifies that we run until we set a rand node
                potential_node = root.get_rand_node()    # get the rand node
                if potential_node is not self:           # make sure we dont set rand to self
                    self.rand = potential_node           # set rand
                    node_set = True                      # break our watchdog loop
        else:
            assert type(node) is Node                    # we were given a value so make sure its the correct type
            self.rand = node                             # then set the variable

    def get_rand_node(self, depth=None):
        # takes an integer depth from 0 to the length of the linked list
        # Danger there be recursion ahead
        if depth is None:                                # if we are not given a depth
            assert self.root is True                     # can only be called without a depth on a root node
            depth = random.choice(range(self.length+1))  # get how far down the list to go +1 because of how range works
        if depth != 0:                                   # if we aren't at the required depth keep going
            return self.next.get_rand_node(depth - 1)
        elif depth == 0:                                 # we made it
            return self

    def __str__(self):
        return str(self.value)                           # return the value of the node as a string


def linked_list_deep_copy(root):
    new_root = Node(root.value, True)                           # define the root of the copied list
    current_original_node = root.next                           # working node on original list
    current_copy_node = new_root                                # working node on copied list

    while current_original_node is not None:                    # while we have more nodes to copy
        current_copy_node.add_node(current_original_node.value) # make a node with the same value as the original next
        new_root.length += 1                                    # increment out new list length
        current_copy_node = current_copy_node.next              # move up the list
        val = current_original_node.rand.value                  # find the value of rand node
        node = new_root                                         # reset a temp node

        while node.value is not val and node.next is not None:  # loop until we find a node in new list with same val
            node = node.next                                    # stepping part

        current_copy_node.rand = node                           # found it
        current_original_node = current_original_node.next      # move the original working element forward

    return new_root                                             # return the copy

if __name__ == '__main__':
    # Generate linked list with defined next and random back links
    root = Node(0, True)            # setup a root node
    node = root                     # allow a stepping variable that doesn't modify root
    for x in range(1, 25):          # add nodes 1-24 for a total of 25 nodes
        node.add_node(x)            # add a new node
        root.length += 1            # iterate the length of the list stored with root
        node = node.next            # set our working node to the next node
        node.set_rand(root)         # set the random for the active node
                                    # this is here as node 0 has no back links and None has no value atribute.

    # Deep Copy list
    copied = linked_list_deep_copy(root)  # so much work for a single function call

    # Compare
    # this is just output and its late
    o_node = root
    c_node = copied
    while o_node is not None:
        print("O Node:{} | Next:{} | Rand:{} || C Node:{} | Next:{} | Rand:{} || O is C {}"
              .format(str(o_node).zfill(2),
                      str(o_node.next).zfill(2),
                      str(o_node.rand).zfill(2),
                      str(c_node).zfill(2),
                      str(c_node.next).zfill(2),
                      str(c_node.rand).zfill(2),
                      o_node is c_node)
              .replace("None", "No"))
        o_node = o_node.next
        c_node = c_node.next
