def find_missing_num(array):
	
	sum_of_array = 0
	sum_of_indexes = 0

	for a in array:
		sum_of_array += a
	for b in range(1, len(array) + 1):
		sum_of_indexes += b

	return sum_of_indexes - sum_of_total

if __name__ == "__main__":

	n = int(input())	
	nums = [int(input()) for _ in range(n)]
	print()
	print(find_missing_num(nums))