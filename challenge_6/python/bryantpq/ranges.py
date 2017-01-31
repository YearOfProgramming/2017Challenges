def get_ranges(a):
    result = []

    if a:
        start = a[0]
        found = False

        for i in range(1, len(a)):
            if a[i] - 1 != a[i - 1]:
                if found:
                    result.append(str(start) + "->" + str(a[i - 1]))
                    found = False
                start = a[i]
            else:
                found = True

        if found:
           result.append(str(start) + "->" + str(a[i]))
 

    return result


def main():
    a = [1, 2, 4, 6, 7, 8, 10, 20, 21, 25, 27, 29, 30, 31, 32]
    print(get_ranges(a))
    b = [1, 2, 3, 4, 8, 9, 10, 12, 13, 14]
    print(get_ranges(b))
    c = [1]
    print(get_ranges(c))
    d = []
    print(get_ranges(d))

if __name__ == "__main__":
    main()
