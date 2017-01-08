import random


class LinkedList:
    class Node:
        def __init__(self, val=None, ran=None):
            self.val = val
            self.next = None
            self.random = ran

        def __str__(self):
            return "{0}".format(self.val)

    def __init__(self):
        self._root = self.Node()
        self._length = 1
        self._current = self._root

    def __len__(self):
        return self._length

    def __repr__(self):
        return "{0}".format(self.print_all(self._root))

    @property
    def root(self):
        return self._root

    @property
    def current(self, value=False):
        return self._current.val if value else self._current

    @property
    def length(self):
        return self._length

    @current.setter
    def current(self, other):
        if isinstance(other, self.Node):
            self._current = other
        else:
            self._current = self.Node(other)

    def add(self, val, ran=None):
        if val is None:
            raise ValueError("You can't have the value None on the value!")
        self._add(val, self.root, ran)

    def _add(self, value, root, ran):
        if root.val is None:
            if root.random is None:
                root.random = ran
            root.val = value
        elif root.next is None:
            if root.random is None:
                root.next = self.Node(value, ran)
            root.next = self.Node(value)
            self._length += 1
        else:
            self._add(value, root.next, ran)

    def next(self, node=None):
        """
        Returns the next value of a node.
        This is a method, so that deep_scan can
        use it recursively.
        :param node:
        :return: Next value of Node.
        """
        if node is None:
            if self._current.next is None:
                raise KeyError("There are no next node.")
            else:
                self._current = self._current.next
        else:
            return node.next

    def deep_copy(self):
        """
        Create a new LinkedList, go through the next method
        add the next value to the new LinkedList.
        Set this instance's current value back to what it was before.
        :return: The new LinkedList instance.
        """
        new = LinkedList()
        new.add(self._root.val, self._root.random)
        current_node = self.current
        self.current = self._root
        while self.current.next is not None:
            new.add(self.next(self.current).val, self.current.random)
            self.current = self.current.next
        self.current = current_node
        return new

    def print_all(self, root):
        empty_lst = [root.val]
        while root.next is not None:
            empty_lst.append(root.next.val)
            root = root.next
            self.print_all(root)
        return empty_lst

    def empty(self):
        self._root = self.Node()
        self._current = self._root
        self._length = 1

