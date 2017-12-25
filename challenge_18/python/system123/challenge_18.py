import numpy as np
from math import factorial

# Allowing Right and Up is the same as allowing Down and Right and starting from the top left corner
# and traversing to the bottom right corner
# Generating the textual desciptions can be done a lot more efficiently, but I continued on with the 
# dynamic programming approach for that too
def number_of_paths(n: int):
	paths = np.empty((n, n, 2), dtype=object)

	# The first row and column only have one solution
	paths[:, :, 0] = np.zeros((n,n))
	paths[0, :, 0] = np.ones(n)
	paths[:, 0, 0] = np.ones(n)

	# Initialise the lists used for building up the string descriptions
	for pos, val in np.ndenumerate(paths[:, :, 1]):
		r, c = pos
		paths[r, c, 1] = []

	paths[1, 0, 1].append("U")
	paths[0, 1, 1].append("R")

	# Use dynamic programming for an O(N^2) solution
	for pos, val in np.ndenumerate(paths[:, :, 0]):
		r, c = pos

		# Generating the string version of the paths
		if r != 0:
			for x in paths[r - 1, c, 1]:
				paths[r, c, 1].append("{}U".format(x))

		if c != 0:
			for x in paths[r, c - 1, 1]:
				paths[r, c, 1].append("{}R".format(x))

		# If we just counting the number of paths then only the next 3 lines are required
		if r == 0 or c == 0:
			continue
		paths[r, c, 0] = paths[r - 1, c, 0] + paths[r, c - 1, 0]

	# Reutrn the total number of paths plus the strings describing each path
	return( [int(paths[-1, -1, 0]), paths[-1,-1, 1]] ) 

# Simple solution for calculating the number of paths for any sized matrix
def number_of_paths_fast(n: int):
	n -= 1
	# This is just binomial combinations
	# Solution is just a set of strings len(2n) of R's and U's where num(R) == num(U) == n
	return( factorial(2*n)//( factorial(n) * factorial(n) ) )

if __name__ == "__main__":
	n = int(input("Enter matrix dimension: "))
	num, routes = number_of_paths( n )
	print( "There are {} possible routes.".format(num) )
	print(routes)
	print(number_of_paths_fast( n ))
