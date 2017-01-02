#!/usr/bin/ruby

input  = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
input_chars = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]

output = input.group_by{|i| i}.to_h.min_by{|k,v| v.count}.first
output_chars = input_chars.group_by{|i| i}.to_h.min_by{|k,v| v.count}.first

puts output
puts output_chars
