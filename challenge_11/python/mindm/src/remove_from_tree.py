#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from btree import BTree


def insertion(args):

    tree = BTree()

    for value in args.strip().split(" "):
        tree.insert(value)

    return tree


def deletion(tree, args):

    for value in args.strip().split(" "):
        tree.remove(value)

    return tree


if __name__ == "__main__":

    args_insert = input("Insert nodes with spaces: ")
    tree = insertion(args_insert)
    tree.tree_print()

    args_delete = input("Which values to delete?: ")
    tree = deletion(tree, args_delete)
    tree.tree_print()
