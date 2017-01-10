#How to Use
Author: William Østensen (wOstensen)

## Squared Sort
The program takes in a sorted list of numbers, including both negative and positive numbers, and 0;
the program's purpose is to return a new list where every number is squared and the new list should be sorted as well

Example:

Given this list: `[1, 4, 5, 10]`, the program should return `[1, 16, 25, 100]`.

A problem arises when you add negative numbers to the program, which would (after squaring the numbers) result in an
incorrect answer. My solution resolves that and makes sure to sort the list correctly.

## Documentation
Simply call the function `squared_sort([list])`, where `list` is your sorted list.
The function creates two lists: `neg` (for the negative numbers) and `pos` (for the positive numbers).
I loop through the inputted list, add the negative numbers in `neg` and positive numbers in `pos`. I reverse `neg` to make it ordered.
Then I go through the lowest number (ie. `[0]` because they are sorted) in each list, and add those to the result list until one of the lists are empty.

Then I return the result list plus the non-empty list.