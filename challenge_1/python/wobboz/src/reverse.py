from sys import argv

if len(argv) == 1:
	print("[usage] reverse needs one argument")
elif len(argv) == 2:
	print(argv[1][::-1])
else:
	print("[usage] reverse only takes one argument")