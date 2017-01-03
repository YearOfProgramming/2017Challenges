array  =  [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
for i in range(0,len(array)):
    temp = array.count(i)
    if temp == 1:
        print(str(array[i]) + " " + "appears once in this array")
        exit
