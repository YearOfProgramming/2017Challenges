class TreeNode:

    def __init__(self,value):
        self._value = value
        self._right_child = None
        self._left_child = None
        
    def print_node(self):
        if self._left_child != None:
            self._left_child.print_node()
        print str(self._value),
        if self._right_child != None:
            self._right_child.print_node()

    def invert_node(self):
        if self._left_child != None:
            self._left_child.invert_node()
        if self._right_child != None:
            self._right_child.invert_node()
        temp_node = self._left_child
        self._left_child = self._right_child
        self._right_child = temp_node