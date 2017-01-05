class Node:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def draw(self):
        '''Prints a preorder traversal of the tree'''
        self._draw(self.root)
        print()

    def _draw(self, node):
        print("(", end="")
        if node != None:
            print(str(node.value) + ", ", end="")
            self._draw(node.l)
            print(", ", end="")
            self._draw(node.r)
        print(")", end="")


    def invert(self):
        self.root = self._invert(self.root)


    def _invert(self, node):
        # find lowest point where nodes can be swapped
        # swap nodes
        if node:
            node.l = self._invert(node.l)
            node.r = self._invert(node.r)
            temp = node.l
            node.l = node.r
            node.r = temp

        return node


    def add(self, vals):
        for val in vals:
            if self.root == None:
                self.root = Node(val)
            else:
                self._add(self.root, val)


    def _add(self, node, val):
        if val < node.value:
            if node.l == None:
                node.l = Node(val)
            else:
                self._add(node.l, val)
        else:
            if node.r == None:
                node.r = Node(val)
            else:
                self._add(node.r, val)


def main():
    t = BinaryTree()
    t.add([4, 2, 7, 1, 3, 6, 9, 11])
    t.draw()
    t.invert()
    t.draw()

if __name__ == "__main__":
    main()
