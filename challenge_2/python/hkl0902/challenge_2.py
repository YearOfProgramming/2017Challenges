'''
Given a list, LST, of integers/characters, finds the one integer/character pair that does not repeat
'''
def findNonRepeaters(lst):
    count = {}
    nonRepeatingInt = None
    nonRepeatingChar = None
    for i in lst:
        try:
            count[i] += 1
        except:
            count[i] = 1
            
    for key, val in count.items():
        if val == 1:
            if isinstance(key, int):
                nonRepeatingInt = key
            else:
                nonRepeatingChar = key

    return (nonRepeatingInt, nonRepeatingChar)

l = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 6, 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd']

(i, c) = findNonRepeaters(l)

if i:
    print(i, end="")
if c:
    print(",", c)
