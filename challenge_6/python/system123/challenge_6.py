a=[1,2,3,4,5,6]

def ranges(input_list):
	data = list(input_list)

	ret = []
	start = None
	end = None

	for x in data:
		if start == None:
			start = end = x
			continue

		if x > (end + 1):
			ret.append("{}->{}".format(start, end))
			start = x
			
		end = x

	if start != None:
		ret.append("{}->{}".format(start, end))

	return(ret)

if __name__ == '__main__':
    ranges(list(input()))