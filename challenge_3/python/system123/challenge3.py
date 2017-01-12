
def find_majority(arr):
	n = len(arr)
	hist = {}

	for x in arr:
		if x in hist.keys():
			hist[x] += 1
			if hist[x] >= n/2:
				return(x)
		else:
			hist[x] = 1

data = list(input("Input CSV data: ").split(","))
print( find_majority(data) )
