from collections import Counter
#extra credit list
# Added 5 to the end so the expected output in instructions would be correct
myList = (2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7,5)

#use counter to see if item is repeated and a list comprehension to store them
print([k for k, v in Counter(myList).items() if v == 1])