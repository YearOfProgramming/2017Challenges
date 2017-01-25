# Squares
###### Java 8

### 1. Approach to Solving the problem

I struggled with this problem for a while. Originally I made a slow solution 
that basically traversed through the array until the number was > than current and placed it there.
This was slow and bad. slack member **zmiller91**'s solution is what I implemented, but only after I fully 
understood his approach. It was very clean and elegant and I learned a lot from it.

### 2. How to compile and run this code

```
javac Squares.java
java Squares
```

### 3. How this program works

Add all negatives squared to position 0 of the negatives list (this is bad I believe
as it results in every value shifting at every insertion) and add all positives to their own list.
Then, start counting through both lists from 0, and while at least one list still has values (index < length)
continue to get the value and add it to the result after comparing it with the negative value at that index.
The way index out of bounds is avoided is by constantly checking if the indexs are < length of their
respective list. If it ever exceeds the length, set that value to MAX_VALUE so it will always be greater than the 
positive or negative value it was compared with, essentially nullifying that index. Values are touched only once
for O(n);