function majority(s::Array)
    # Create a counter dictionary Dict(element => number of times element appears in input array)
    counter = Dict()
    length_s = 0
    # Count the number of times each element in s appears
    for i in s
       length_s += 1
       if i in keys(counter)
           counter[i] += 1
       else
           counter[i] = 1
       end
    end
    # Loop through the items in the counter dictionary, return majority element
    for (key, value) in counter
       if value > length_s/2
           return key
       end 
    end
    # If no majority element, return a message:
    return "No majority element"
end


# The example case from the prompt
println(majority([2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]))
# And another case
println(majority([1,1,1,2,3,4,1,1,1]))
# And a case with no majority element
println(majority([9,9,9,9,8,8,8,8]))
