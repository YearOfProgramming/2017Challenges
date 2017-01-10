def find_the_diff(s, t):
    
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
