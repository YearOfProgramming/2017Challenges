def missingNo(inputList):

	minInt = min(inputList)
	maxInt = max(inputList)

	if minInt != 0:
		return 0

	else:
		return sum(range(minInt,(maxInt + 1))) - sum(inputList)