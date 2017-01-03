"""I have combine the two array in exemple from README.md in challenge_2 and then find the string/int repeated only once in the array with set"""
array = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7,2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
unique =set([x for x in array if array.count(x) == 1])
print (unique)
