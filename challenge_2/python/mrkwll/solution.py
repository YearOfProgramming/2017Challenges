def singletons(array=[]):
    s = set([x for x in array if array.count(x) == 1])
    for elem in s:
        print elem


part1 = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7]
part2 = [2, 'a', 'l', 3, 'l', 4, 'k', 2, 3, 5, 4, 'a', 6, 'c', 4, 'm', 6, 'm', 'k', 9, 10, 9, 8, 7, 8, 10, 7]

singletons(part1)
singletons(part2)
