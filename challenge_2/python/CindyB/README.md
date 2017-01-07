#Single Number
###### Python 2.7.9

### 1. Approch to Solving the problem

I want to solve this problem with a linear solution. So, I cannot afford nested loops.
I can use a data structure with time complexity at worst O(n) in insert and access time.

In the first place, I wanted to use the unique character of key in dictionnaries to find the single number.
It would have implied the dictionnary creation from array with count as value for any value in array.

In my process to learn Python, I decided to read more about some structures and functions.
This is how I find out about map function which is a good fit for this kind of problem.
I kept the "count" concept but with a better implementation I believe.

### 2. How to compile and run this code

Assuming you are within the directory under my name

```
$ python src/singleNumber.py
```

### 3. How this program works

You only need to run the program to see the output. No input needed.