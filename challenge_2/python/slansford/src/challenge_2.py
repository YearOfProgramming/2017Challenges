#prints the occurence that does not repeat
#in the given array. Uses Python 3.6.0

given_array = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]

for i in given_array:
	if given_array.count(i) == 1:
		print(i)