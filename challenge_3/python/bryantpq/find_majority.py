def find_majority(a):
    d = {}
    l = len(a)
    for i in a:
        if i in d:
            d[i] += 1
            if d[i] > l / 2:
                return i
        else:
            d[i] = 1

    return


if __name__ == "__main__":
    a = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]
    print(find_majority(a))
