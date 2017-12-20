Warning: This documentation is extremely verbose, i was bored
# Find the missing integer
This program will return the missing integer from an array of integers
The array of integers does not need to be in numerical order (per the readme instructions)

To run, run the command `ruby missing_num.rb` from the same director as the `missing_num.rb` file

# Process

The `ints` array is initialized with an array of un-ordered integers, as well as variables called `missing` and `counter`. The counter variable will serve as an increment tracker in our loop.
The `missing` variable will store the missing number.

A loop is initialized, looping for the same amount of times as the count of our ints array. The reason I don't use `ints.each do |int|` is because i do not need the `|int|` variable in the loop. It seems like a waste to initialize it and not use it.
Each time the loop goes around, it will check to see if the counter is included in the `ints` array. The counter is incremented at the end of the loop, so it's a convenient way to check for number inclusion. If the number we are checking for is not included in the array, it's stored in the `missing` variable. Because we know only 1 integer will be missing from the range (per the readme instructions), we can use a `Fixnum` variable. If it was possible for there to be more than one missing numbers, we could store them in an array, and push them on using `missing.push(counter)`
At the end, we print out the missing number
