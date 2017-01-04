__author__ = "Loran425"


def majority(data):
    count = {}
    output = None  # Have a value to return if there is no majority
    for char in data:
        # Dirty dirty dirty
        try:
            count[char] += 1
        except KeyError:
            count[char] = 1
    for x in count.keys():
        if count[x] >= len(count) // 2:
            output = x
    return output


if __name__ == '__main__':
    array = [2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7,
             7, 7, 7]
    print(majority(array))
