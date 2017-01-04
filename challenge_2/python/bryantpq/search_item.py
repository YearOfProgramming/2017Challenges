def search_item(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    if 1 not in d.values():
        print("No unique values found!")
        return

    for k, v in d.items():
        if v == 1:
            print("Unique value is " + str(k))

    return
        

if __name__ == "__main__":
    a = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
    search_item(a)
    b = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]
    search_item(b)
