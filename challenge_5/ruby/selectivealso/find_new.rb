require "./methods.rb"

s = "abcd"
t = "abcde"

complete_string = ElementsArray.new(s, t)

puts complete_string.find_diff_chars
