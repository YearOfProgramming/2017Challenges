#Get counter to count the items in our list
from collections import Counter

#given list for challenge
myList = (2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7)

#Use a list comprehension and floor division to see if occurrences is greater to or equal than half of the items
print([k for k,v in Counter(myList).items() if v >= len(myList)//2])


