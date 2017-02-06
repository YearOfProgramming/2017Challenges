class Node:
    """
    val: int = The value of the node.
    r: Node  = The value of the right node.
    l: Node  = The value of the left node.
    """
    def __init__(self, val):
        self.val = val
        self.r = None
        self.l = None

    @property
    def _val(self):
        return self.val

    @_val.setter
    def _val(self, value):
        self.val = value


class Tree:
    def __init__(self, root: int):
        self.root = Node(root)

    @property
    def _root(self):
        return self.root

    def __iadd__(self, other):
        if type(other) == int:
            self.add(other)
        elif type(other) == list:
            for i in other:
                if type(i) != int:
                    raise TypeError("You can only have integers in your list!")
                else:
                    self.add(i)
        return self

    def invert(self, node):
        node.r, node.l  = node.l, node.r
        if node.r is not None:
            self.invert(node.r)
        if node.l is not None:
            self.invert(node.l)

    def add(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            self._add(val, self.root, node)

    def _add(self, val, root, node):
        if val <= self.root.val:
            if root.l is None:
                root.l = node
            else:
                self._add(val, root.l, node)
        else:
            if root.r is None:
                root.r = node
            else:
                self._add(val, root.r, node)

    def print_simple(self):
        print(f"  {self.root._val}  \n / \  \n{self.root.l._val}   {self.root.r._val}")