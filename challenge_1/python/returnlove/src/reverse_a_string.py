# read input string from user
input_string = raw_input("enter any string")

# solution 1
# create a variable to store the reversed string
reversed_string = ""

# loop through the input in reverse order and append each letter
for l in xrange(len(input_string)-1, -1, -1):
	reversed_string += str(input_string[l])

print('Solution 1: ',reversed_string)


# solutin 2
print('Solution 2: ',''.join(reversed(input_string)))

# solution 3
print('Solution 3: ',input_string[::-1])