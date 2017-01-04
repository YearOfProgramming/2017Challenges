require "./methods.rb"

s = "abcd"
t = "abcde"

# This concatenates the string, then splits each letter into an element of an array
# because only one letter is added to the new string, we know that it will be unique
# we use the method from challenge 2 to find the unique character
puts "#{s}#{t}".split('').find_unique