(Python 3.5)
Function "majority_element" finds element found > floor(n/2) times in a list of items of length n.

The function "majority_element_old" uses a dictionary to create a frequency array from the original list, 
with key/value pairs comprised of:
{list_item: item_frequency}

Complexity is O(n), because it will iterate once through the original list (n) to populate the 
frequency array, and once through the frequency array (n) to find the majority element.

Version 2: "majority_element" now uses Counter to check frequency of items in list.
Runs built-in efficiency comparison between the two, with two optional test cases.
