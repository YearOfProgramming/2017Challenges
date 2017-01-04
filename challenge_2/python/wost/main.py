"""
Python 3.6:
  :: Counts all the instances of all the elements in a list.
  :: Returns all the instances with a count of 1.
"""

def find_one_in_list(a_list):
  a_dict = {}
  
  for char in a_list:
    if char not in a_dict.keys():
      a_dict[char] = 1
    else:
      a_dict[char] += 1
    
  for letter in a_dict.keys():
    if a_dict[letter] == 1:
      print(letter, end=" ")
  print()
      
def main():
  # Returns 6, 7.
  find_one_in_list([5, 4, 3, 4, 5, 6, 1, 3, 1, 7, 8, 8])
  # Returns b.
  find_one_in_list(["a", "b", "c", "a", "c", "W", "W"])
  # Returns A, 5, r.
  find_one_in_list(["A", "b", "d", "r", 4, 5, 4, "b", "d"])
  # Returns nothing.
  find_one_in_list([])
  
if __name__ == "__main__":
  main()
