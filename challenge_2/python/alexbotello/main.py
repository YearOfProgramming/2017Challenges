if __name__ == '__main__':
    N = int(input()) # How many items in the list?
    array = [int(input()) for _ in range(N)] # Enter ints

    print("\nThe single number is ", end='')
    print(min(array, key=array.count))
