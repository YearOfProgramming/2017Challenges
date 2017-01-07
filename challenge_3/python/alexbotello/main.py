from collections import Counter

if __name__ == "__main__":
    N = int(input())
    array = [input() for _ in range(N)]

    print('\nThe most common number is ', end='')
    print(list(dict(Counter(array).most_common()))[0])
    
