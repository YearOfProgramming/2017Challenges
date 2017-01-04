string = "hello"
reversedstring = []
index = len(string)
print(index)
for i in string:
    reversedstring.append(string[index-1])
    index = index - 1
print(reversedstring)
                                 
