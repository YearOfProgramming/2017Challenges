import sys

def reverse(string):
	return string[::-1]

if __name__ == '__main__':
	print(reverse(" ".join(sys.argv[1:])))
