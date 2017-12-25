array = list(input().split(","))

def find_nodup(arr):
	s = {}
	ret = []

	for x in arr:
		if x in s.keys():
			s[x] += 1
		else:
			s[x] = 1

	for k, v in s.items():
		if v == 1:
			ret.append(k)

	return(ret)

print(find_nodup(array))
