__author__ = "Loran425"


def once(list):
    count = {}
    for char in list:
        try:
            count[char] += 1
        except KeyError:
            count[char] = 1
    return ' '.join([str(x) for x in count.keys() if count[x] == 1])

if __name__ == '__main__':
    array = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7]
    print(once(array))
