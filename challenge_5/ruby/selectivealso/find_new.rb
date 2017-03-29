require "./methods.rb"

s = "abcd"
t = "abcde"

complete_string = UniqueFinder.new(s, t)

puts complete_string.find_unique
