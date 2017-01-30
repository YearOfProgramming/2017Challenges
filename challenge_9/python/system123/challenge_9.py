from collections import deque

def squared_sort(input_list):
	negs = deque([])
	pos = deque([])
	sorted = []

	for x in input_list: #O(n)
		if x < 0:
			negs.append(x**2)
		else:
			pos.append(x**2)

	n = None
	p = None
	for i in range(0, len(input_list)): #O(n)
		if pos and p == None:
			p = pos.popleft()
		if negs and n == None:
			n = negs.pop()

		if ((n != None) and (n <= p)) or (p == None):
			sorted.append(n)
			n = None
		else:
			sorted.append(p)
			p = None

	return(sorted)

if __name__ == "__main__":
	print(squared_sort(input()))
