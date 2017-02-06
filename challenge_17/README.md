Change
======
Idea
-----
How many ways can you divide 1000 cents into quarters, dimes, nickles and pennies? We're about to find out. Your job today is to create a program which takes an integer from standard input and determines the number of ways that number can be achieved, using the change listed above.

For example, how many ways could we make 100 cents? 
* 4 Quarters
* 2 Quarters, 5 Dimes
* 100 Pennies
* ...

You must output the number of ways in which change can be given for the input.

Testing
-----
100 cents would yield 64207 possible combinations

50 cents would yield 309 possible combinations

150 cents would yield 13322380 possible combinations

I would give more examples but I did it the O(N!) way so it's physically impossible to compute the number of ways to achieve 1000 cents before the universe implodes.