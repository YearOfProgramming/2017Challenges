function rangefinder(t::Array)
    # List of ranges
    ranges = []
    if length(t) < 2
        return ranges
    end
    
    # Start at the beginning of the input t
    rangestart = t[1]
    rangeend = t[1]
    
    # Loop through all elements of t in sequence
    for i in 2:length(t)
        # Check if the next entry is in the same range as the current range start
        if rangeend+1 == t[i]
            rangeend = t[i]
        else
            # If not, check that the range has length > 0
            if rangeend > rangestart
                push!(ranges, string(string(rangestart), "->", string(rangeend)))
            end
            # Ignore ranges of length 0
            rangestart = t[i]
            rangeend = t[i]
        end
#        println(rangestart, rangeend, ranges)
    end
    if rangeend > rangestart
        push!(ranges, string(string(rangestart), "->", string(rangeend)))
    end
#    println(rangestart, rangeend, ranges)
    return ranges
end

# Try the function a few times on a few test cases
t1 = [1,2,3,4,8,9,10,12,13,14]
t2 = [1,2,3,4,9,10,15]
t3 = [1,2]
t4 = [1]
t5 = [1, 2, 3, 14, 25, 30, 31, 32]
t6 = [5,6,9,10,12,13,15,16,18,19,25,30]
println("Input: ", t1)
println("Output: ", rangefinder(t1))
println("Input: ", t2)
println("Output: ", rangefinder(t2))
println("Input: ", t3)
println("Output: ", rangefinder(t3))
println("Input: ", t4)
println("Output: ", rangefinder(t4))
println("Input: ", t5)
println("Output: ", rangefinder(t5))