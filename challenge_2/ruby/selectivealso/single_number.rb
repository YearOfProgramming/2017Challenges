nums = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
count = Hash.new(0)

nums.each do |num|
  count[num] += 1
end

puts count.key(1)