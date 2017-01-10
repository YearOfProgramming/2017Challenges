from Node import Tree
from Node import Node

def main():
    tree = Tree(2)

    tree += [1, 2, 3]

    tree.print_simple()
    tree.invert(tree._root)
    tree.print_simple()

if __name__ == "__main__":
    main()
