inOpt = input("Input the list separated by spaces or 'default' to use the default list.\n")

if inOpt == 'default':
	list = [str(k) for k in [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]]	#default list
else:
	list = [str(j) for j in inOpt.strip().split()]	#strip whitespace, split into characters, convert to string

strCounts = {}	#initialize a dictionary

for i in list:	#iterate over strings in input list

	if i in strCounts:			#if the item is present, increment the count
		strCounts[i] += strCounts[i]
	else:
		strCounts[i] = 1		#otherwise, set count to 1

print("These have not been repeated:")

for i in list:
	if strCounts[i] == 1:		#print all items in dictionary with count 1
		print(i,' ')
