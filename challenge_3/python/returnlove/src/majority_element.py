def find_majority_element(input_list):
	majority_condition = len(input_list)/2
	# print(majority_condition)	
	my_dict = {}
	# print(input_list)
	# convert input list into dictionary, key being the element and value is the count
	for element in input_list:
		if element not in my_dict.keys():
			my_dict[element] = 1
		else:
			my_dict[element] += 1

	# print(my_dict)

	for k in my_dict.keys():
		if my_dict[k] > majority_condition:
			print(k)


def main():
	my_list = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]
	find_majority_element(my_list)


if __name__ == "__main__":
	main()