arr = ['a', 'a', 'b','b', 1, 2, 2, 3, 3, 'z', 'z']
answer = ''
for i in range(len(arr)):
	if(arr.count(arr[i]) == 1):
		answer = arr[i]
print(answer)


