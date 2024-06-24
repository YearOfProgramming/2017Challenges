a = ['a', 'b', 'c', 2, 3, 5, 'a', 2, 'c', 5, 'b']
rep = []
non_rep = []
for i in a:
	if i in rep:
		continue	
	elif i in non_rep:
		rep.append(i)
		non_rep.remove(i)
	else:
		non_rep.append(i)
print(non_rep)
