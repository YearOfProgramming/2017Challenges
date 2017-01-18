"""
Each root has two subtrees, each subtree may have a root
Each tree has the format ['parent',
                          ['child1',
                           ['child1.1'],['child1.2']],
                          ['child2',
                           ['child2.1'],['child2.2']]]
"""

import itertools

def reverse(tree):
    subtree = tree.copy()
    if len(subtree[1]) < 2 and len(subtree[2]) < 2:
        return [subtree[0], subtree[2], subtree[1]]
    elif len(subtree[1]) < 2:
        return [subtree[0], [reverse(subtree[2])], subtree[1]]
    elif len(subtree[2]) < 2:
        return [subtree[0], subtree[2], [reverse(subtree[1])]]
    else:
        return [subtree[0], reverse(subtree[2]), reverse(subtree[1])]


test = [4,
        [2,
         [1], [3]],
        [7,
         [6], [9]]
       ]

def create_large_tree():
    """
    Create a tree with up to 4 levels of nodes to show that implementation scales, enter less then 15
    """
    value_of_nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
    tree = ''
    depth = 0
    count = 0

    while depth < 4:
        if depth == 0:
            tree = [value_of_nodes[0], [], []]
            depth += 1
            count += 1
        elif depth == 1:
            for i in [1,2]:
                tree[i] = [value_of_nodes[count], [], []]
                count += 1
            depth += 1
        elif depth == 2:
            for i,j in itertools.product([1,2], repeat=depth):
                tree[i][j] = [value_of_nodes[count], [], []]
                count += 1
            depth += 1
        elif depth == 3:
            for i, j, k in itertools.product([1,2], repeat=depth):
                tree[i][j][k] = [value_of_nodes[count], [], []]
                count += 1
            depth += 1
    return tree


print(test)
test_rev = reverse(test)
print(test_rev)
print(reverse(test_rev))

test2 = create_large_tree()
print(test2)
test_rev2 = reverse(test2)
print(test_rev2)
print(reverse(test_rev2))