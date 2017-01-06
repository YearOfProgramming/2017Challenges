ints = [1,2,3,4,8,9,10,13,15,16,17]
starts = []
ranges = {}

# This loop finds the start of each range and throws it into an array called starts
ints.each do |int|
  # Find the index of the int
  index = ints.find_index(int)

  # check if start of range
  if int - 1 != ints[index - 1]
    starts.push(index)
  end
end


x = 0
# Writes a new range element for each range, with the key being the start, and the value being the end
(starts.count - 1).times do
  ranges[ints[starts[x]]] = ints[starts[x + 1] - 1]
  x = x + 1
end

# The loop above checks the element ahead of the looped element, which throws an error
# This gets the last element 'from the other way' to solve that.
# I think this is the worst code i have ever written
# r/badcode
ranges[ints[starts[-1]]] = ints[-1]

# Checks each range for repeats.
# If the key and value are the same, it's the same number,
# not a range, so it gets removed
ranges.each do |start, ending|
  if start == ending
    ranges.delete(start)
  end
end

# Print out the ranges
puts ranges.inspect