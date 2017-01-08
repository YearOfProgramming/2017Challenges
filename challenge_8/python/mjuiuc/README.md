#Challenge 8 Solution in Python

Well, the problem itself wasn't too bad I don't think. Just deep copying a list right? The harder part was copying over the random pointers which is something I thought might be easy until I actually started doing it. I sort of cheated and used a dictionary to map all of the values of the pointers in the copied list to their respective nodes. I ran through the original list once and copied all the nodes to a new list, then I went through it again to assign all of the random pointers... I don't know how i would've done this without pythons dictionary. I'm sure there's a nice way to do it, but I couldn't figure it out. Oh well :/

#Testing
I created a unit test whith three seperate test cases. To use them, simply copy my folder and re write the code under the solution function in the solution.py file. To run the test cases, run the test.py file.