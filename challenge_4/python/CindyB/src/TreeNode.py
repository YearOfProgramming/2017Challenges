class TreeNode:

    def __init__(self,value):
        self._value = value
        self._right_child = None
        self._left_child = None

    def get_value(self):
        return self._value

    def set_right_child(self,child):
        self._right_child = child

    def set_left_child(self,child):
        self._left_child = child

    def get_right_child(self):
        return self._right_child
    
    def get_left_child(self):
        return self._left_child
        
    def print_node(self):
        if self.get_left_child() != None:
            self.get_left_child().print_node()
        print str(self.get_value()),
        if self.get_right_child() != None:
            self.get_right_child().print_node()

    def invert_node(self):
        if self.get_left_child() != None:
            self.get_left_child().invert_node()
        if self.get_right_child() != None:
            self.get_right_child().invert_node()
        tempNode = self.get_left_child()
        self.set_left_child(self.get_right_child())
        self.set_right_child(tempNode)