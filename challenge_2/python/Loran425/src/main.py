__author__ = "Loran425"

from collections import Counter

def once(list):
    count = Counter(list)
    return [x for x in count.keys() if count[x] == 1]

if __name__ == '__main__':
    array = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7]
    print(' '.join(str(x) for x in once(array)))
