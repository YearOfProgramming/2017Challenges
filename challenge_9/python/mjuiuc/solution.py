def solution(nums):
	# create list to hold the negative vars
	negatives = list()
	positives = list()
	newlist = list()

	for i in xrange(0, len(nums)):
		if nums[i] >= 0:
			positives.append(abs(nums[i])**2)
		else:
			negatives.append(abs(nums[i])**2)
	# reverse the list of negatives so that they're in asscending order
	negatives.reverse()
	# append the min value of each of the list until one of them is empty
	while (len(negatives) != 0) and (len(positives) != 0):
		if negatives[0] > positives[0]:
			newlist.append(positives.pop(0))
		elif negatives[0] < positives[0]:
			newlist.append(negatives.pop(0))
		else:
			newlist.append(positives.pop(0))
			newlist.append(negatives.pop(0))
	# when one list is empty, append the rest of the other
	if len(negatives) != 0:
		newlist = newlist + negatives
	if len(positives) != 0:
		newlist = newlist + positives
	# done
	return newlist
