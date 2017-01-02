#!/usr/bin/ruby

if ARGV[0].to_i != 0
  puts "Must be a string"
  abort
end

puts ARGV[0].reverse
