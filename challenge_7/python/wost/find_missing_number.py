def find_biggest(a):
	biggest = a[0]
	for i in a:
		if i >= biggest:
			biggest = i
	return biggest

def find_missing_number(c):
	b = find_biggest(c)
	v = set(range(0, b)) - set(c)
	return list(v)[0] if v != set() else None

print(find_missing_number([1, 3, 2, 4]))
print(find_missing_number([0, 2, 3, 4, 5]))
