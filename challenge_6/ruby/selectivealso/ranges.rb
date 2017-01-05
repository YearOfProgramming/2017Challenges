require './methods.rb'

ints = [1,2,3,4,8,9,10,12,13,14]
count = 0
ranges = []

ints.each do
  if ints.start_of_range(count)
    $start_range = ints[count]
  end

  count = count + 1

  if ints.end_of_range(count)
    end_range = ints[count]
    ranges.push("#{$start_range}->#{end_range}")
  end
end
puts ranges.inspect