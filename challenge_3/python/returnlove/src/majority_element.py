"""
To find the majority elements in a list.
	Counts number of times each element is present in the list
	prints all the elements which are present more than half of the list
"""

import math

def find_majority_element(input_list):
	majority_condition = math.floor(len(input_list)/2)
	# print(majority_condition)	
	my_dict = {}
	result = []
	for element in input_list:
		if element not in my_dict.keys():
			my_dict[element] = 1
		else:
			my_dict[element] += 1

	for k in my_dict.keys():
		if my_dict[k] > majority_condition:
			result.append(k)
	return result

def main():
	my_list = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]
	print(find_majority_element(my_list))

if __name__ == "__main__":
	main()