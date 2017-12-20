import sys
my_list=sys.argv[1]

for x in range(0,len(my_list)+1):
    if x not in my_list:
        print(x)
