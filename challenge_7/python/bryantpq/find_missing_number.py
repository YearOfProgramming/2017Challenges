#!/usr/bin/python3

def find_num(a):
    total = sum(range(len(a) + 1))

    for n in a:
        total = total - n

    return total


def main():
    print(find_num([1, 3, 4, 0]))
    print(find_num([0, 1, 2, 4]))
    print(find_num([1, 2, 3]))
    print(find_num([0, 1, 2, 3, 4]))
    print(find_num([0]))
    print(find_num([1]))
    print(find_num([]))


if __name__ == "__main__":
    main()

