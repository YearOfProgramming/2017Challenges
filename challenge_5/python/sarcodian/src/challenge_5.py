def find_the_diff(s, t):
    '''
    s: string, a string made up of lower case letters
    t: string, a string made up of shuffled up s plus one additional char
    returns: char, the single element string that was not in s
    '''
    
    t_dict = {}
    s_dict = {}
    
    for i in s:
        s_dict[i] = s_dict.get(i, 0) + 1
    
    for i in t:
        t_dict[i] = t_dict.get(i, 0) + 1
    
    for i in t_dict.keys():
        if t_dict[i] > s_dict.get(i, 0):
            return i
            
s = "aaaaab"
t = "aaaaaab"
print(find_the_diff(s,t))
