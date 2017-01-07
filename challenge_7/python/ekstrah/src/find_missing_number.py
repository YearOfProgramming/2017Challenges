def find_missing_number(num: list) -> int:
    missing = 0
    for i in range(0, len(num)):
        for j in range(0, len(num)): #{
            if i == num[j]: #{
                missing = 1
                break
            #}
        if missing == 0:
            return i
        missing = 0
    #}



if __name__ == '__main__':
    print(find_missing_number([0,2,3,4,1,8,7,6,5,9,11,10,12,13,15]))
