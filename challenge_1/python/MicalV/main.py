def reverseStr(string):
    y = len(string)
    charList = []
    for x in range(y):
        charList.insert(0,string[x])
    for z in range(y):
        print(charList[z], end="")

reverseStr("Testing testing 1 2 3")