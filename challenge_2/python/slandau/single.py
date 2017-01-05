#!/usr/bin/env python3


def find_single(input: list) -> str:
    # Create a container (dictionary) to store the keys mapped to the number of times they occur
    container = {}
    # Go through the input list and fill the container
    for piece in input:
        if piece in container:
            container[piece] += 1
        else:
            container[piece] = 1

    # Go through the container and return the first value we see that has a value of one
    for piece in container:
        if container[piece] == 1:
            return piece

    # O(N) + O(N) is still O(N)

if __name__ == '__main__':
    print(find_single([2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]))
    print(find_single([2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]))