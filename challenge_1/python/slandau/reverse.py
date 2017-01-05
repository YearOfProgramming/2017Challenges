#!/usr/bin/env python3


def reverse(input: str) -> str:
    if len(input) < 2:
        return input

    return input[-1] + reverse(input[1:-1]) + input[0]


def reverse_iter(input: str) -> str:
    ret = ""
    for i in range(len(input)):
        ret += input[len(input)-1-i]

    return ret


if __name__ == '__main__':
    string = input("String to be reversed: ")
    print(reverse(string))
