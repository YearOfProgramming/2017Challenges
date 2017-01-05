__author__ = "Loran425"


def majority(data):
    count = {}
    for char in data:
        if char not in count.keys():
            count[char] = 1
        else:
            count[char] += 1
            if count[char] >= len(data) // 2:
                return char  # Break as soon as we find a majority

    return None  # Return None if there is no majority

if __name__ == '__main__':
    array = [2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7,
             7, 7, 7]
    print(majority(array))
