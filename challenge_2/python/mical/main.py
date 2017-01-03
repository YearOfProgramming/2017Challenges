#02/01/2017

def noRepeats(things):
    for x in things:
        amount = list.count(x)
        if amount == 1:
            print(x)
        else:
            continue

things = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]
noRepeats(things)
