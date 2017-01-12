"""
To find the single number in a list.
	Counts number of times each element is present in the list
	prints all the elements which are present only once
"""

# function takes input list and converts to a dictionary, key being the element and value is the count
def single_number(input_list):
	my_dict = {}
	for element in input_list:
		if element in my_dict.keys():
			my_dict[element] += 1
		else:
			my_dict[element] = 1
	# find the keys in dict where the count is one
	for k in my_dict.keys():
		if my_dict[k] == 1:
			print(k)

def main():
	my_list = [1,2,2,3,3,4,4,5,5,6,6,'x','x','y']
	single_number(my_list)


if __name__ == "__main__":
	main()