arr = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]
answer = 0
for i in arr:
	if(arr.count(arr[i]) > len(arr)/2):
		answer = arr[i]
print(answer)
