function unrepeat{Array}(input::Array)
    holder=Set()
    repeats=Set()

    for i in input
        if i in holder
            push!(repeats, i)
        else
            push!(holder, i)
        end
    end
    println(collect(setdiff(holder, repeats))[1])
end

i1 = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
i2 = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]
unrepeat(i1)
unrepeat(i2)
