#02/01/2017

def noRepeats(list):
    for x in list:
        amount = list.count(x)
        if amount == 1:
            print(x)
        else:
            continue

list = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]
noRepeats(list)