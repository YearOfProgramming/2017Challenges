function findTheDifference(s::ASCIIString, t::ASCIIString)
    # Find the difference between the two lower-case strings s and t, where t has one additional randomly-inserted character
    # First sort both s and t as lists of characters:
    slist = Array([i for i in s])
    tlist = Array([i for i in t])
    sort!(slist)
    sort!(tlist)
    # Now, just to be sure, let's check to see if s and t are equal:
    if join(tlist) == join(slist)
        # This is analogous to the None variable in python
        return Union{}
    end
    # Loop through all the items in tlist, comparing them one by one to the items in slist
    for i in eachindex(slist)
        si = slist[i]
        ti = tlist[i]
        if si != ti
            return ti
        end
    end
    return tlist[end]
end        

println(findTheDifference("abcde", "abcdef"))
println(findTheDifference("abbbcccddddf", "fcbdddbbaccbd"))
println(findTheDifference("typewriter", "typewriter"))
