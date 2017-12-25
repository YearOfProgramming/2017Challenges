function findMissing(l::Array)
    n = length(l)
    return Int(n*(n+1)/2) - sum(l)
end

t1 = [0,1,2,4];
println( "Input: ", t1)
println( "Output: ", findMissing(t1))
t2 = [1,2,3];
println( "Input: ", t2)
println( "Output: ", findMissing(t2))
t3 = [1,3,4,0];
println( "Input: ", t3)
println( "Output: ", findMissing(t3))