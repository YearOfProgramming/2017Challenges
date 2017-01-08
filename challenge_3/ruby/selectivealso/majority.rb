nums = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]
counts = Hash.new(0)

# For each element in nums, add 1 to the number tally
nums.each do |num|
  counts[num] += 1
end
# Get the element with the highest value
majority = counts.max_by{|k,v| v}

puts "The majority element was #{majority[0]} with #{majority[1]} occurences"
