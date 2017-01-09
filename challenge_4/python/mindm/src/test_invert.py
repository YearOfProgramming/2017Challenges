#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from btree import BTree, Node, flip_tree

tree = BTree(4,
             Node(2,
                  Node(1),
                  Node(3)),
             Node(7,
                  Node(6),
                  Node(9)))

tree.tree_print()

flip_tree(tree)
print("\nFlipping tree...")
tree.tree_print()
