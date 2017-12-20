
combs = 0
lst = []
def path(length, width, x, y, path_string):
    if x == length and y == width:
        global combs
        lst.append(path_string)
        combs += 1
    elif x == length:
        path(length, width, x, y + 1, path_string + 'U')
    elif y == length:
        path(length, width, x + 1, y, path_string + 'R')
    else:
        path(length, width, x, y + 1, path_string + "U")
        path(length, width, x + 1, y, path_string + "R")

path(2,2, 0, 0, "")
print(lst)


