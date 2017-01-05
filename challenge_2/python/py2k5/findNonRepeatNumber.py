#!/usr/bin/python

arr = [2,3,4,3,5,4,6,4,6,9,10,9,2,8,7,8,10,7]

dict1={}
for elem in arr:
	dict1.setdefault(elem, 0)
	dict1[elem] = dict1.get(elem) + 1

for a in dict1.keys():
	if dict1.get(a) == 1:
		print a




