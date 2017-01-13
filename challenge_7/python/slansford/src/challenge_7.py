def missingNo(inputList):

	minInt = min(inputList)

	if minInt != 0:
		return 0

	for i in inputList:
		if minInt in inputList:
			minInt += 1
		else:
			return minInt
			break