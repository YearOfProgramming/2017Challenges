from collections import Counter
dictionary = dict(Counter([2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]))
revdictionary = {value: key for key, value in dictionary.items()}
print(revdictionary.get(1))

