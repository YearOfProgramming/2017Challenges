class node: #{
    def __init__(self, val): #{
        self.value = val
        self.left = None
        self.right = None
    #}
    def insert_lc(self, value): #{
        self.left = node(value)
    #}
    def insert_rc(self, value): #{
        self.right = node(value)
    #}
    def right_child(self): #{
        if self.right != None:
            return True
        return False
    #}
    def left_child(self): #{
        if self.left != None:
            return True
        return False
    #}
    def insert(self, cur_node, val): #{
        if cur_node.value == val:
            return
        elif cur_node.value < val :
            if cur_node.right_child():
                cur_node.right.insert(cur_node.right,val)
            else:
                cur_node.insert_rc(val)
        else:
            if cur_node.left_child():
                cur_node.left.insert(cur_node.left,val)
            else:
                cur_node.insert_lc(val)
    #}
    def reverse(self): #{
        self.left, self.right = self.right, self.left
        if self.left != None:
            self.left.reverse()
        if self.right != None:
            self.right.reverse()
    #}

    def traverse(rootnode): #{
        thislevel = [rootnode]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print (n.value, end="")
                if n.left:
                    nextlevel.append(n.left)
                if n.right:
                    nextlevel.append(n.right)
            print("")
            thislevel = nextlevel
    #}

#}

if __name__ == "__main__": #{
    aList = [4, 2, 1, 3, 7, 9, 6]
    root_node = node(aList[0])

    for num in aList: #{
        root_node.insert(root_node, num)
    #}
    root_node.traverse()
    root_node.reverse()
    root_node.traverse()
#}
