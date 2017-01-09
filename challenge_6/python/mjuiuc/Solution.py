#	Writing solution for this range problem

class solution(object):
	def compRange(nums):
		#	nums is of type list()
		#	nums contains only integers in ascending order
		#	this function should return the list of collapsed ranges

		if nums == None:
			return None
		if len(nums) == 1:
			return []

		resList = list()
		start = nums[0]
		end = 0
		newList = list()
		for i in xrange(1,len(nums)):
			if nums[i] != int(nums[i-1] + 1):
				end = nums[i-1]
				resList.append("{s}->{e}".format(s = start, e = end))
				start = nums[i]

			if i == len(nums) - 1:
				end = nums[i]
				resList.append("{s}->{e}".format(s = start, e = end))

		return resList
