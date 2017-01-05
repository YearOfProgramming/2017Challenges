from Node import Tree
from Node import Node

def main():
    tree = Tree(2)

    tree.add(1)
    tree.add(2)
    tree.add(3)

    tree.print_simple()
    tree.invert(tree._root)
    tree.print_simple()

if __name__ == "__main__":
    main()
