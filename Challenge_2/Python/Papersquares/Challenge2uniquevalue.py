
list = [2,3,4,2,3,5,4,6,4,6,9,'a',10,9,8,7,8,10,7]

newlist = []
for i in list:
	if list.count(i) == 1:
		newlist.append(i)
print newlist
