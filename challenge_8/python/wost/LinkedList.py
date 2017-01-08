import random


class LinkedList:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None
            self.random = None

        def __repr__(self):
            return self.val

    def __init__(self):
        self._root = self.Node()
        self._length = 1
        self._current = self._root

    def __len__(self):
        return self._length

    def __repr__(self):
        self.print_all(self._root)

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

    def set_random(self):
        i, ran = 1, random.randint(1, self._length)
        root = self._root
        while root.next is not None:
            if i == ran:
                return root
            i += 1
            root = root.next
        return root

    def add(self, val):
        self._add(val, self.root)

    def _add(self, value, root):
        if root.val is None:
            root.val = value
            root.random = self.set_random()
        elif root.next is None:
            root.next = self.Node(value)
            root.next.random = self.set_random()
            self._length += 1
        else:
            self._add(value, root.next)

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
            return node.next.val

    def deep_copy(self):
        """
        Create a new LinkedList, go through the next method
        add the next value to the new LinkedList.
        Set this instance's current value back to what it was before.
        :return: The new LinkedList instance.
        """
        new = LinkedList()
        new.add(self.root.val)
        current_node = self.current
        self.current = self._root
        while self.current.next is not None:
            new.add(self.next(self.current))
            self.current = self.current.next
        self.current = self.root
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

