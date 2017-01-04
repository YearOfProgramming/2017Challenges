class BTree:
    def __init__(self, b_tree_list=list()):
        self.b_tree_list = b_tree_list
        self.levels = len(b_tree_list)

    def visualise(self):
        for index, level in enumerate(self.b_tree_list):
            spacing = 2 ** (self.levels - index) - 1
            print(((spacing-1)//2)*' ', end='')
            for node in level:
                if node is None:
                    print(' ', end='')
                else:
                    print(node, end='')
                print(spacing * ' ', end='')
            print('')  # newline

    def invert(self):
        for level in self.b_tree_list:
            level.reverse()


example_tree = BTree([
    [4],
    [2, 7],
    [1, 3, 6, 9]])

example_tree.visualise()
example_tree.invert()
example_tree.visualise()
