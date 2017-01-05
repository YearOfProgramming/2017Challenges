def find_missing_number(num: list) -> int:
    num.sort()
    for i in range(0, len(num)):
        if i != num[i]:
            return i

if __name__ == '__main__':
    print(find_missing_number([5,4,3,2,1,8,7,6]))
