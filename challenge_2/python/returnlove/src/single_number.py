# function takes input list and converts to a dictionary, key being the element and value is the count
def single_number(input_list):
	# return(input_list)
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



## Below is the solition but not with linear time.

# my_list = [9,9,1,0,2,5,0,10,1,9,10,2,5,'x',100]
# my_list = sorted(my_list)
# # print(sorted(my_list))
# dup = []
# for i in range(len(my_list)):
# 	actual_num = my_list[i]
# 	for j in range(i+1, len(my_list)):
# 		# print(j)
# 		compare = my_list[j]
# 		if(actual_num == compare):
# 			# print(my_list[i],'dup')
# 			dup.append(my_list[i])
# 			break

# # print(dup)
# unique = []
# for e in my_list:
# 	if e not in dup:
# 		# print(e)
# 		unique.append(e)	

# print('Single Number values are: ',unique)