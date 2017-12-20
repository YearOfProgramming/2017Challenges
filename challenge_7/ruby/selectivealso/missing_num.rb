ints = [0,1,2,5,4,3,7,8,9]
missing = 0
counter = 0

ints.count.times do
  if !ints.include?(counter)
    missing = counter
  end
  counter = counter + 1
end

puts "The missing number is #{missing}"