
def rev_num(x):
	rev = 0

	while(x != 0):
		# Move all digits in rev up to the next significant place
		# Append the last digit of x
		rev = (rev * 10) + (x % 10)
		# Drop the last digit of x
		x = x//10

	return(rev)


def is_palindrome(x):
	return(x - rev_num(x) == 0)