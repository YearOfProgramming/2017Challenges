# ints = [1,2,3,4,8,9,10,12,13,14]
ints = [1,2,3,4,8,9,10,13,15,16,17]
starts = []
ranges = []

ints.each do |int|
  # Find the index of the int
  index = ints.find_index(int)

  # check if start of range
  if int - 1 != ints[index - 1]
    starts.push(index)
  end

end

x = 0
(starts.count - 1).times do
  ranges.push("#{ints[starts[x]]}->#{ints[starts[x + 1] - 1]}")
  x = x + 1
end



ranges.push("#{ints[starts[-1]]}->#{ints[-1]}")

puts ranges.inspect

# ints ---------------
# [1, 2, 3, 4, 8, 9, 10, 12, 13, 14]
# starts ---------------
# [0, 4, 7]
# ranges ---------------
# []

# puts "ints ---------------"
# puts ints.inspect
# puts "starts ---------------"
# puts starts.inspect
# puts "ranges ---------------"
# puts ranges.inspect