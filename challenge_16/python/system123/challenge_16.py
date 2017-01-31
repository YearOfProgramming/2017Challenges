from collections import Counter
from math import factorial

def num_unique_perms(input_str):
	n = len(input_str)
	hist = Counter(input_str)

	# Equal to 1 to prevent div zero errors if there are no repeated characters
	reps = 1
	for c, cnt in hist.items():
		reps *= factorial(cnt)

	return( factorial(n)//reps )

def perms(perm_set, input_str, prefix=''):
	if len(input_str) == 0:
		perm_set.add(prefix)
	else:
		for i in range(len(input_str)):
			perms(perm_set, input_str[0:i] + input_str[i+1:], prefix + input_str[i])

if __name__ == "__main__":
	print( "{} -> {}".format("abc", num_unique_perms("abc")) )
	print( "{} -> {}".format("abcdefgh", num_unique_perms("abcdefgh"))  )

	lst = set()
	perms(lst, "abcd")
	print( "{} -> {}".format(lst, len(lst)))
