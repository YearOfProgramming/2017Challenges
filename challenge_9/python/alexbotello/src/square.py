def square_soft(input_list):
    """
    Returns a list with all values squared and sorted
    """
    squared = []

    # Separate negative and positive values
    # Reverse the negative array to preserve order
    # ex: [-3, -2, -1] -> [-1, -2, -3] -> [1, 4, 9]
    neg = [x**2 for x in input_list if x < 0]
    pos = [x**2 for x in input_list if x >= 0]
    neg.reverse()

    # While loop will exit when squared takes in every value from input_list
    # pop() each value after appending as to avoid using a counter variable
    # and possibily getting an IndexError
    while len(squared) != len(input_list):
        # Add the rest of pos array if neg is empty
        if not neg:
            squared.extend(pos)
        # Add the rest of neg array if pos is empty
        elif not pos:
            squared.extend(neg)

        elif pos[0] >= neg[0]:
            squared.append(neg.pop(0))

        else:
            squared.append(pos.pop(0))

    return squared

if __name__ == "__main__":

    # Test your own implementation
    n = int(input()) # Number of elements in list
    array = [int(input()) for _ in range(n)]

    print(square_soft(array))
