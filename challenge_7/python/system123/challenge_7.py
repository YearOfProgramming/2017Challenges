
def find_missing_number(data: list):

	# Formula for the sum of digits between 1 and N 
	# We know we start at 0 and that we have N-1 digits so the same formula can be used
	sum_expected = (len(data)*(len(data) + 1)) >> 1
	sum_actual = 0

	for i in data:
		sum_actual += i

	return( sum_expected - sum_actual )

if __name__ == '__main__':
	print( find_missing_number(input()) )