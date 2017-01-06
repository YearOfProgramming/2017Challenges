Find Missing Number solution:

The program first takes an unsorted list of numbers from 0 to n, of which one number is missing.

The find_missing_number function takes in one paramater (a list in this case), and first sorts the list. A new list is created with the name newlist.

In line 7, the sum of the current list is subtracted from the complete list. That is, we subtract n-1 list from n list to find the missing number.