"""
Each root has two subtrees, each subtree may have a root
Each tree has the format ['parent',
                          ['child1',
                           ['child1.1'],['child1.2']],
                          ['child2',
                           ['child2.1'],['child2.2']]]
"""
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


test_rev = reverse(test)
print(test_rev)
print(reverse(test_rev))