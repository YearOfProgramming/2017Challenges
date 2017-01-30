# list1 = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
list1 = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7,5] #extra credit

for index in range(0,len(list1)):
    if list1.count(index) == 1:
        print index