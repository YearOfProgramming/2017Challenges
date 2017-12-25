def findthedifference(s,t):
    # Find the difference between the two lower-case strings s and t, where t has one additional randomly-inserted character
    # First sort both s and t as lists of characters:
    slist = sorted(list(s))
    tlist = sorted(list(t))
    # Now, just to be sure, let's check to see if s and t are equal:
    if ''.join([i for i in slist]) == ''.join([i for i in tlist]):
        return None
    # Loop through all the items in tlist, comparing them one by one to the items in slist
    for si in slist:
        ti = tlist.pop(0)
        if ti != si:
            return ti
    # And in case the difference is at the end of the sorted string t
    return tlist[-1]

if __name__=="__main__":
    # Test case: returns f
    print findthedifference('abcde', 'abcdef')
    # Test case: returns b
    print findthedifference('abbbcccddddf', 'fcbdddbbaccbd')
    # Test case: identical strings
    print findthedifference('typewriter', 'typewriter')
