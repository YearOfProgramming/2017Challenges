def solution(nums):
	n = len(nums) + 1
	sums = 0
	Summation = 0
	for i in nums:
		sums += i
	for i in xrange(0,n+1):
		Summation += i
	return (Summation - sums) % n