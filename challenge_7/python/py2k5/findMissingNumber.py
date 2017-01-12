
def main():
	numbers = [ 0,1,3,4,2,5,7 ]
        tot = len(numbers)
	if 0 not in numbers: 
		print 0
	else:
		for num in numbers:
			if num +1 < tot and num+1 not in numbers:
				print num + 1
				break

if __name__ == '__main__':
	main()
