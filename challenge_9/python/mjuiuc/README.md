#Solution

The idea behind what the solution should be didn't take super long to think about, but writing the algorithm to do it took quite a bit of time. I worked out the idea that all the negatives in the list are just positives in descending order so I needed to sperate them from the original list and reverse them so they were in ascending order along with the positive numbers. Putting the numbers back in the correct order caused me to use a stack of sorts. The top of the stack is represented as list index 0. I basically loop through both negative and positive stacks until on is empty. after that's done, I check to see if there's any left in the opposite stack and then add those numbers to the end. Making sure I worked out the edge cases was pretty difficult.

While going through both negative and positive stacks, I had to find the min value and push that item to the new list. I think this is the bulk of where my logic goes, so I'll share it here.

``` python

	while (len(negatives) != 0) and (len(positives) != 0):
		if negatives[0] > positives[0]:
			newlist.append(positives.pop(0))
		elif negatives[0] < positives[0]:
			newlist.append(negatives.pop(0))
		else:
			newlist.append(positives.pop(0))
			newlist.append(negatives.pop(0))
```
Hopefully that doesn't completely give away the solution. The nice thing about python is that this looks like it's an abstraction from something, but it isn't! I'm just starting to notice that now and it makes me realize how neat python really is!

#Testing
I've included four test cases with my solution. As always, I write the test cases before I write the actual solution as I think it's good practice.
-	First test is an empty list
-	Second test is a list of all positives
-	Third test is a list of all negatives
-	Fourth test is a list composed of both + and - but it's shorter than the second and third test

Runtimes for your function on each test are printed to the console.
This time, I've included a solution_template.py file where you can write your solution. Just change the name to solution.py when you're ready to use the unit test I've made.