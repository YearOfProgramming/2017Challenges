#
# Find the Single Number
#


def single_number(array):
    single_num = []
    repeated_num = []
    temp = array[:]
    for x in array:
        temp.remove(x)
        if x not in temp and x not in repeated_num:
            single_num.append(x)
        else:
            repeated_num.append(x)
    return single_num


if __name__ == '__main__':
    array_1 = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7]
    array_2 = [2, 'a', 'l', 3, 'l', 4, 'k', 2, 3, 4, 'a', 6, 'c', 4, 'm', 6, 'm', 'k', 9, 10, 9, 8, 7, 8, 10, 7]
    single_num_1 = single_number(array_1)
    single_num_2 = single_number(array_2)
    print(single_num_1)
    print(single_num_2)
