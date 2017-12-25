def square_sort(inputList):

	pos = [i**2 for i in inputList if i >= 0]
	neg = [i**2 for i in inputList if i < 0]
	neg = neg[::-1]

	outputList = []

	while len(outputList) != len(inputList):

		if not neg:
			outputList += pos

		elif not pos:
			outputList += neg

		elif pos[0] >= neg[0]:
			outputList.append(neg[0])
			neg.remove(neg[0])

		else:
			outputList.append(pos[0])
			pos.remove(pos[0])

	return outputList
