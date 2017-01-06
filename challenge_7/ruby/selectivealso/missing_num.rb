ints = [0,1,5,4,6,3,8,7,9]
missing = 0
counter = 0

ints.count.times do
  if !ints.include?(counter)
    missing = counter
  end
  counter = counter + 1
end

puts "The missing number is #{missing}"